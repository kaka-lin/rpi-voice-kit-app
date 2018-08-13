import _ from 'lodash';
import React, { Component } from 'react';
import { ListView, Text, StyleSheet, View } from 'react-native';
import { connect } from 'react-redux';
import { BleManager } from 'react-native-ble-plx';
import ListItem from './ListItem';
import { Button, CardSection } from './common';
import { bleScanInfo, bleScanStart, bleScanStop } from '../actions';

class BleList extends Component {
  // Creating BLE Manager
  componentWillMount() {
    this.manager = new BleManager();

    this.crearDataSource(this.props);
  }

  componentWillReceiveProps(nextProps) {
    // nextProps are the next set of props that this component
    // will be render with
    // this.props is still the old set of props

    this.crearDataSource(nextProps);
  }

  componentWillUnmount() {
    this.manager.destroy();
    delete this.manager;
  }

  crearDataSource({ bleDevices }) {
    const ds = new ListView.DataSource({
      rowHasChanged: (r1, r2) => r1 !== r2
    });

    this.dataSource = ds.cloneWithRows(bleDevices);
  }

  onStartScanPress() {
    this.scan();
  }

  onStopScanPress() {
    this.manager.stopDeviceScan();
    this.props.bleScanStop();
    this.props.bleScanInfo("Stop Scan!");
  }

  scan() {
    this.manager.startDeviceScan(null, null, (error, device) => {
      this.props.bleScanInfo("Scanning...")

      if (error) {
        this.props.bleScanInfo(error.message)
        return
      }

      this.props.bleScanStart(device);
    });
  }

  renderRow(bleDevice) {
    return <ListItem bleDevice={bleDevice} />;
  }

  render() {
    return (
      <View style={styles.container}>
        <Text style={styles.text}>Ble Scanner</Text>
        <Text style={styles.infoText}>{this.props.info}</Text>

        <CardSection>
          <Button onPress={this.onStartScanPress.bind(this)}>
            Start
          </Button>

          <Button onPress={this.onStopScanPress.bind(this)}>
            Stop
          </Button>
        </CardSection>

        <ListView
          enableEmptySections
          dataSource={this.dataSource}
          renderRow={this.renderRow}
        />

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
    backgroundColor: '#fff'
  },
  infoText: {
    fontSize: 16,
    color: 'blue',
    textAlign: 'center',
    backgroundColor: '#fff'
  },
});

const mapStateToProps = (state) => {
  /*
  const bleDevices = _.map(state.bleDevices, (val, uid) => {
    return { ...val, uid }; // { shift: 'Monday', name: 'Kaka', id: 'abcdefg'};
  });
  */

  var bleDevices = Object.assign({}, state.bleDevices);
  const info = state.bleState.info;

  return { bleDevices, info };
}

export default connect(mapStateToProps, { bleScanInfo, bleScanStart, bleScanStop })(BleList);
