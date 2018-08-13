import React, { Component } from 'react';
import { View, Text, Image, StyleSheet } from 'react-native';
import { Card, CardSection, Button } from './common';
import { Buffer } from 'buffer';

class BleModule extends Component {
  componentWillMount() {
    console.log(this.props.bleDevice);
    this.connect();
  }

  connect() {
    const device = this.props.bleDevice;

    return new Promise((resolve, reject) =>{
      device.connect()
        .then((device) => {
          console.log("Connect Success!");
          return device.discoverAllServicesAndCharacteristics();
        })
        .then((device) => {
          return this.fetchServicesAndCharacteristicsForDevice(device);
        })
        .then((services) => {
          console.log('fetchServicesAndCharacteristicsForDevice',services);
          this.getUUID(services)
          resolve();
        })
        .catch((error) => {
          console.log('Connect Fail', error);
          reject(error);
        })
    });
  }

  async fetchServicesAndCharacteristicsForDevice(device) {
    var servicesMap = {};
    var services = await device.services();
    //console.log(services);

    for (let service of services) {
      var characteristicsMap = {};
      var characteristics = await service.characteristics();
      //console.log(characteristics);

      for (let characteristic of characteristics) {
        characteristicsMap[characteristic.uuid] = {
          uuid: characteristic.uuid,
          isReadable: characteristic.isReadable,
          isWritableWithResponse: characteristic.isWritableWithResponse,
          isWritableWithoutResponse: characteristic.isWritableWithoutResponse,
          isNotifiable: characteristic.isNotifiable,
          isNotifying: characteristic.isNotifying,
          value: characteristic.value
        }
      }

      servicesMap[service.uuid] = {
        uuid: service.uuid,
        isPrimary: service.isPrimary,
        characteristicsCount: characteristics.length,
        characteristics: characteristicsMap
      }
    }

    return servicesMap;
  }

  getUUID(services){
    this.readServiceUUID = [];
    this.readCharacteristicUUID = [];
    this.writeWithResponseServiceUUID = [];
    this.writeWithResponseCharacteristicUUID = [];
    this.writeWithoutResponseServiceUUID = [];
    this.writeWithoutResponseCharacteristicUUID = [];
    this.nofityServiceUUID = [];
    this.nofityCharacteristicUUID = [];

    for(let i in services){
      //console.log('service',services[i]);
      let charchteristic = services[i].characteristics;
      for(let j in charchteristic){
        //console.log('charchteristic',charchteristic[j]);
        if(charchteristic[j].isReadable){
          this.readServiceUUID.push(services[i].uuid);
          this.readCharacteristicUUID.push(charchteristic[j].uuid);
        }
        if(charchteristic[j].isWritableWithResponse){
            this.writeWithResponseServiceUUID.push(services[i].uuid);
            this.writeWithResponseCharacteristicUUID.push(charchteristic[j].uuid);
        }
        if(charchteristic[j].isWritableWithoutResponse){
            this.writeWithoutResponseServiceUUID.push(services[i].uuid);
            this.writeWithoutResponseCharacteristicUUID.push(charchteristic[j].uuid);
        }
        if(charchteristic[j].isNotifiable){
            this.nofityServiceUUID.push(services[i].uuid);
            this.nofityCharacteristicUUID.push(charchteristic[j].uuid);
        }
      }
    }

    console.log('readServiceUUID',this.readServiceUUID);
    console.log('readCharacteristicUUID',this.readCharacteristicUUID);
    console.log('writeWithResponseServiceUUID',this.writeWithResponseServiceUUID);
    console.log('writeWithResponseCharacteristicUUID',this.writeWithResponseCharacteristicUUID);
    console.log('writeWithoutResponseServiceUUID',this.writeWithoutResponseServiceUUID);
    console.log('writeWithoutResponseCharacteristicUUID',this.writeWithoutResponseCharacteristicUUID);
    console.log('nofityServiceUUID',this.nofityServiceUUID);
    console.log('nofityCharacteristicUUID',this.nofityCharacteristicUUID);
  }

  write() {
    let hexValue = new Buffer([1]).toString('base64');
    let transactionId = 'writeWithoutResponse';

    console.log("test1: ", hexValue, typeof(hexValue));

    const device = this.props.bleDevice;
    device.writeCharacteristicWithResponseForService(this.writeWithResponseServiceUUID[0],
      this.writeWithResponseCharacteristicUUID[0], hexValue, transactionId)
      .then((characteristic) => {
        console.log('Write Success', hexValue);
      }, (error) => {
        console.log('write fail',error);
      })

  }

  render() {
    return (
      <View style={styles.container}>
        <CardSection>
          <Text style={{fontSize: 20}}>Voice Kit</Text>
          <Image
            style={{height: 100, width: 100}}
            source={require('../imgs/voice-kit.png')}
          />
        </CardSection>

        <CardSection>
          <Button onPress={this.write.bind(this)}>
            Ble test
          </Button>

          <Button>
            Voice Kit
          </Button>
        </CardSection>
      </View>
    );
  }
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    flexDirection: 'column',
    margin: 10,
  },
});

export default BleModule;
