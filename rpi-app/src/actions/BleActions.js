import {
  BLE_SCAN_INFO,
  BLE_SCAN_START,
  BLE_SCAN_STOP
} from './types';

const devices = []

export const bleScanInfo = (text) => {
  return {
    type: BLE_SCAN_INFO,
    payload: text
  }
}

export const bleScanStart = (device) => {
  var isSame = false;
  for (let i = 0; i < devices.length; i++) {
    if (devices[i].id == device.id) {
      isSame = true;
      break;
    }
  }

  if (!isSame) {
    devices.push(device);
  }

  return {
    type: BLE_SCAN_START,
    payload: devices
  }
}

export const bleScanStop = () => {
  return {
    type: BLE_SCAN_STOP,
    payload: []
  }
}
