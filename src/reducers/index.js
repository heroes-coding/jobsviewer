import { combineReducers } from 'redux'
import { createStore, applyMiddleware } from 'redux'
import ReduxPromise from 'redux-promise'
import openJob from './open_job_reducer'
import listings from './listings_reducer'

const rootReducer = combineReducers({
  openJob,
  listings
})

// making store here so I can access it outside of react components elsewhere
const createStoreWithMiddleware = applyMiddleware(ReduxPromise)(createStore)
const store = createStoreWithMiddleware(rootReducer)

export default store
