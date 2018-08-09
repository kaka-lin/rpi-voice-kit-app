import { BLE_SCAN_START } from '../actions/types';

const INITIAL_STATE = {
  id: '',
  name: '',
  info: 'Stop Scan!'
};

export default (state = INITIAL_STATE, action) => {
  switch(action.type) {
    case BLE_SCAN_START:
      return { ...state, info: action.payload };
    default:
      return state
  }
}
