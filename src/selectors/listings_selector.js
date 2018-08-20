import { createSelector } from 'reselect'
const listings = state => state.listings

const getSortedListings = (listings) => {
  console.log({listings})
  if (!listings) return []
  listings.sort((x,y) => y.timestamp - x.timestamp) // y.month - x.month || y.day - x.day)
  return listings
}

export default createSelector(
  listings,
  getSortedListings
)
