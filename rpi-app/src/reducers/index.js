import { combineReducers } from 'redux';
import BleReducer from './BleReducer';
import BleStateReducer from './BleStateReducer';

export default combineReducers({
  bleDevices: BleReducer,
  bleState: BleStateReducer
});
