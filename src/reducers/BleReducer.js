import {
  BLE_SCAN_START,
  BLE_SCAN_STOP
} from '../actions/types';

var INITIAL_DEVICE = [];

export default (device = INITIAL_DEVICE, action) => {
  switch(action.type) {
    case BLE_SCAN_START:
      return action.payload;
    case BLE_SCAN_STOP:
      return action.payload;
    default:
      return device;
  }
}
