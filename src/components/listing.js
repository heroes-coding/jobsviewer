import React from 'react'

const Listing = ({day,month,id,link,location,region,state,title}, updateListing) => {
  return (
    <div
      className="listing"
      key={id}
      onClick={() => updateListing(id)}
    >
      <div className="listing_date">{`${month} / ${day}`}</div>
      <div className="listing_title">{title}</div>
      <div className="listing_location">{`${region},${state} (${location})`}</div>
    </div>
  )
}

export default Listing
