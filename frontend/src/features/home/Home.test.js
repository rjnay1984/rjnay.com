import React from 'react';
import configureMockStore from 'redux-mock-store';
import thunk from 'redux-thunk';
import { render } from '@testing-library/react';
import { Provider } from 'react-redux';
import { Home } from './Home';

const middlewares = [thunk]
const mockStore = configureMockStore(middlewares)

describe('Home Component', () => {

  it('has the loading state', () => {
    const store = mockStore({
      homeContent: {
        loading: true,
        content: {},
        hasErrors: false
      }
    })

    const { getByText } = render(
      <Provider store={store}>
        <Home />
      </Provider>
    )

    expect(getByText('Loading...')).toBeInTheDocument();
  });

  it('loads the content', () => {

    const store = mockStore({
      homeContent: {
        loading: false,
        content: {
          body: 'Home page content'
        },
        hasErrors: false
      }
    })

    const { getByText } = render(
      <Provider store={store}>
        <Home />
      </Provider>
    )

    expect(getByText('fail test')).toBeInTheDocument();
  })

  it('has errors', () => {
    const store = mockStore({
      homeContent: {
        loading: false,
        content: {},
        hasErrors: true,
      }
    })

    const { getByText } = render(
      <Provider store={store}>
        <Home />
      </Provider>
    )

    expect(getByText('Error loading content.')).toBeInTheDocument();
  })
});

