import { UPDATE_LISTINGS } from '../actions'
const initialState = []

export default function(state = initialState, action) {
  if (action.type === UPDATE_LISTINGS) return action.listings
  return state
}
