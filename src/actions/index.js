import axios from 'axios'

export const UPDATE_DISPLAYED_JOB = 'UPDATE_DISPLAYED_JOB'
export const UPDATE_LISTINGS = 'update_listings'
export const UPDATE_PREFERENCES = 'update_preferences'

export const updatePreferences = (key,value) => { type: UPDATE_PREFERENCES, key, value }

export const updateDisplayedJob = async(job_id) => {
  const response = await axios.get(`http://localhost:4100/body/${job_id}`)
  const job = response.data[0]
  return { type: UPDATE_DISPLAYED_JOB, job }
}

export const updateJobListings = async(search_terms = []) => {
  const response = await axios.get(`http://localhost:4100/search/${search_terms.join(",")}`)
  const listings = response.data
  return { type: UPDATE_LISTINGS, listings }
}
