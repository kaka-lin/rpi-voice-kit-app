import React, { Component } from 'react';
import { AppRegistry, View } from 'react-native';
import { Provider } from 'react-redux';
import { createStore, applyMiddleware } from 'redux';
import { name as appName } from '../app.json';
import { Header } from './components/common';
import reducers from './reducers';
import BleList from './components/BleList';

class App extends Component {
  render() {
    const store = createStore(reducers)

    return (
      <Provider store={store}>
        <View style={{ flex: 1}}>
          <Header headerText={'RPi BLE'} />
          <BleList />
        </View>
      </Provider>
    );
  }
}

AppRegistry.registerComponent(appName, () => App);
