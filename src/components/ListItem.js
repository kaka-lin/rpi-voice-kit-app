import React, { Component } from 'react';
import { Text, TouchableWithoutFeedback, View } from 'react-native';
import { Actions } from 'react-native-router-flux';
import { CardSection, Card } from './common';

export default class ListItem extends Component {
  onRowPress() {
    Actions.bleModule({ bleDevice: this.props.bleDevice });
  }

  render() {
    const { id, name } = this.props.bleDevice;

    return (
      <TouchableWithoutFeedback onPress={this.onRowPress.bind(this)}>
        <View>
          <CardSection>
            <Text style={styles.textStyle}>
              id: {id}
            </Text>
          </CardSection>

          <CardSection>
            <Text style={styles.textStyle}>
              name: {name}
            </Text>
          </CardSection>
        </View>
      </TouchableWithoutFeedback>
    );
  }
}

const styles = {
  textStyle: {
    fontSize: 13,
    paddingLeft: 15
  }
};
