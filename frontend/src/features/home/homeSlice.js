import { createSlice } from '@reduxjs/toolkit';

export const initialState = {
  loading: false,
  content: {},
  hasErrors: false,
}

const homeSlice = createSlice({
  name: 'home',
  initialState,
  reducers: {
    getHomePage: state => {
      state.loading = true
    },

    getHomePageSuccess: (state, { payload }) => {
      state.loading = false
      state.content = payload
    },

    getHomePageFailure: state => {
      state.hasErrors = true
    },
  }
})

// Three actions generated from the slice
export const { getHomePage, getHomePageSuccess, getHomePageFailure } = homeSlice.actions

export const homeSelector = state => state.homeContent;

export default homeSlice.reducer;

export function fetchHomeContent() {
  return async dispatch => {
    dispatch(getHomePage())

    try {
      const response = await fetch('http://localhost:8000/api/v2/pages/3/');
      const data = await response.json();

      dispatch(getHomePageSuccess(data))
    } catch (error) {
      dispatch(getHomePageFailure())      
    }
  }
}
