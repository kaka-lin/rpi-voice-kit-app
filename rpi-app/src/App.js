import React, { Component } from 'react';
import { AppRegistry, View } from 'react-native';
import { Provider } from 'react-redux';
import { createStore, applyMiddleware } from 'redux';
import { name as appName } from '../app.json';
import reducers from './reducers';
import Router from './Router';

class App extends Component {
  render() {
    const store = createStore(reducers)

    return (
      <Provider store={store}>
        <Router />
      </Provider>
    );
  }
}

AppRegistry.registerComponent(appName, () => App);
