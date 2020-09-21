import { configureStore } from '@reduxjs/toolkit';
import counterReducer from '../features/counter/counterSlice';
import homeReducer from '../features/home/homeSlice';

export default configureStore({
  reducer: {
    counter: counterReducer,
    homeContent: homeReducer,
  },
});
