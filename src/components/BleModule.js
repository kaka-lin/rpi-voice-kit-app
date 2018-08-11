import React, { Component } from 'react';
import { View, Text } from 'react-native';

class BleModule extends Component {
  constructor(props) {
    super(props);
    this.device = this.props.bleDevice;
  }
  componentWillMount() {
    console.log(this.device);
  }
  render() {
    return (
      <View>
        <Text>BleModule</Text>
      </View>
    );
  }
}

export default BleModule;
