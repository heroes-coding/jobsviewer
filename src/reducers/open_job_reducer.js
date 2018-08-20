import { UPDATE_DISPLAYED_JOB } from '../actions'
const initialState = window.localStorage.openJob ? JSON.parse(window.localStorage.openJob) : null

export default function(state = initialState, action) {
  if (action.type === UPDATE_DISPLAYED_JOB) {
    window.localStorage.openJob = JSON.stringify(action.job)
    return action.job
  }
  return state
}
