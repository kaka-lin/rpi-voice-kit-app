import React, { Component } from 'react';
import { Text, TouchableWithoutFeedback, View } from 'react-native';
//import { Actions } from 'react-native-router-flux';
import { CardSection, Card } from './common';

export default class ListItem extends Component {
  /*
  onRowPress() {
    Actions.employeeEdit({ employee: this.props.employee });
  }
  */

  render() {
    const { id, name } = this.props.bleItem;

    return (
      <TouchableWithoutFeedback>
        <Card>
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
        </Card>
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
