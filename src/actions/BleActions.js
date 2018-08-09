import { BLE_SCAN_START } from './types';

export const bleScanStart = (text) => {
  return {
    type: BLE_SCAN_START,
    payload: text
  }
}
