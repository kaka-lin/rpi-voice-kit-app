import {
  BLE_SCAN_INFO,
} from '../actions/types';

const INITIAL_STATE = {
  info: 'Stop Scan!'
};

export default (state = INITIAL_STATE, action) => {
  switch(action.type) {
    case BLE_SCAN_INFO:
      return { ...state, info: action.payload };
    default:
      return state;
  }
}
