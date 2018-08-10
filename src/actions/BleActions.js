import {
  BLE_SCAN_INFO,
  BLE_SCAN_START,
  BLE_SCAN_STOP
} from './types';

export const bleScanInfo = (text) => {
  return {
    type: BLE_SCAN_INFO,
    payload: text
  }
}

export const bleScanStart = (items, device) => {
  var isSame = false;
  for (let i = 0; i < items.length; i++) {
    if (items[i].id == device.id) {
      isSame = true;
      break;
    }
  }

  if (!isSame) {
    items.push(device);
  }

  return {
    type: BLE_SCAN_START,
    payload: items
  }
}

export const bleScanStop = () => {
  return {
    type: BLE_SCAN_STOP,
    payload: []
  }
}
