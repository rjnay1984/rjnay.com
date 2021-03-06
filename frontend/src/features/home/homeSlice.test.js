import thunk from 'redux-thunk';
import reducer, { initialState, fetchHomeContent, getHomePage, getHomePageSuccess, getHomePageFailure } from './homeSlice';

describe('home slice', () => {
  describe('reducer, action creators, and selectors', () => {
    it('should return the initial state on first run', () => {
      // Arrange
      const nextState = initialState;

      // Act
      const result = reducer(undefined, {});

      // Assert
      expect(result).toEqual(nextState);
    });

    it('should return the loading state', () => {
      // Arrange

      // Act
      const nextState = reducer(initialState, getHomePage());

      // Assert
      const rootState = { homeContent: nextState };
      expect(rootState).toEqual({
        homeContent: {
          loading: true,
          content: {},
          hasErrors: false,
        }
      });
    });

    it('should return the error state', () => {
      // Arrange

      // Act
      const nextState = reducer(initialState, getHomePageFailure());
      
      // Assert
      const rootState = { homeContent: nextState }
      expect(rootState).toEqual({
        homeContent: {
          loading: false,
          content: {},
          hasErrors: true,
        }
      });
    });

    it('should fetch home page content', () => {
      // Arrange
      const payload = { content: '<p>Home page content</p>' };

      // Act
      const nextState = reducer(initialState, getHomePageSuccess(payload));

      // Assert
      const rootState = { homeContent: nextState };
      expect(rootState).toEqual({
        homeContent: {
          loading: false,
          content: payload,
          hasErrors: false,
        }
      });
    });
  })
});
