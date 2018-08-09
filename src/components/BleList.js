import _ from 'lodash';
import React, {Component} from 'react';
import { ListView, Text, StyleSheet, View } from 'react-native';
import { connect } from 'react-redux';
import { BleManager } from 'react-native-ble-plx';
import ListItem from './ListItem';
import { Button, CardSection, Card } from './common';
import { bleScanStart } from '../actions';

class BleList extends Component {
  // Creating BLE Manager
  componentWillMount() {
    this.manager = new BleManager();

    //this.crearDataSource(this.props);
  }

  componentWillUnmount() {
    this.manager.destroy();
    delete this.manager;
  }

  onStartScanPress() {
    this.scanAndConnect();
  }

  scanAndConnect() {
    this.manager.startDeviceScan(null, null, (error, device) => {
      this.props.bleScanStart("Scanning")

      if (error) {
        this.props.bleScanStart(error.message)
        return
      }
    });
  }

  /*
  crearDataSource({ info }) {
    const ds = new ListView.DataSource({
      rowHasChanged: (r1, r2) => r1 !== r2
    });

    this.dataSource = ds.cloneWithRows(info);
  }

  renderRow(info) {
    return <ListItem ble={info} />;
  }
  */

  render() {
    return (
      <View style = {styles.container}>
        <Text style = {styles.text}>Ble Scanner</Text>
        <Text style = {styles.infoText}>{this.props.info}</Text>

        <CardSection>
          <Button onPress={this.onStartScanPress.bind(this)}>
            Start
          </Button>

          <Button>
            Stop
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
  text: {
    fontSize: 20,
    textAlign: 'center',
  },
  infoText: {
    fontSize: 16,
    color: 'blue',
    textAlign: 'center',
  },
});

const mapStateToProps = (state) => {
  const { id, name, info } = state.bleItems

  return { id, name, info }
}

export default connect(mapStateToProps, { bleScanStart })(BleList);
