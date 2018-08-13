import React from 'react';
import { Router, Stack, Scene, Actions } from 'react-native-router-flux';
import BleList from './components/BleList';
import BleModule from './components/BleModule';

const RouterComponent = () => {
  return (
    <Router>
      <Stack key="root" hideNavBar>
        <Scene key="main">
          <Scene key="bleList" component={BleList} title="RPi BLE" initial />
          <Scene key="bleModule" component={BleModule} title="Ble Module" />
        </Scene>
      </Stack>
    </Router>
  )
}

export default RouterComponent;
