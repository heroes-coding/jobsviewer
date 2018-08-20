import React, { Component } from 'react'
import logo from './logo.svg'
import axios from 'axios'
import { connect } from 'react-redux'
import {updateDisplayedJob, updateJobListings, updatePreferences } from './actions'
import ListingsSelector from './selectors/listings_selector'
import * as styles from './style/style.css'
import SearchBar from './containers/search_bar'
import '../node_modules/font-awesome/css/font-awesome.min.css'
import '../node_modules/bootstrap/dist/css/bootstrap.min.css'
import Listing from './components/listing'
import Posting from './components/posting'
import DropDown from './components/dropdown'
import SitesList from './updater/sites_list'
window.console.log({SitesList})

class App extends Component {
  constructor(props) {
    super(props)
    this.state = { page: 1, saved: false }
    this.updateListing= this.updateListing.bind(this)
    this.updateSearch= this.updateSearch.bind(this)
    this.markApplied = this.markApplied.bind(this)
    this.updatePreferences = this.updatePreferences.bind(this)
    this.selectPage = this.selectPage.bind(this)
  }
  toggleSaved() {
    const saved = !this.state.saved
    this.setState({...this.state, saved: saved})
  }
  selectPage(page) {
    this.setState({...this.state, page})
  }
  updatePreferences(key,value) {
    this.props.updatePreferences(key,value)
  }
  componentWillMount() {
    this.props.updateJobListings()
  }
  updateSearch(terms) {
    terms = terms.split(" ").filter(x => x)
    this.props.updateJobListings(terms)
    this.setState({...this.state, page: 1})
  }
  updateListing(id) {
    this.props.updateDisplayedJob(id)
  }
  async markApplied(id,applied) {
    // this is a little hacky.  I am not bothering with the entire state to update this but directly interfacing with the database.
    const applyRequest = `http://localhost:4100/apply/${id},${applied}`
    console.log(applyRequest)
    await axios.get(applyRequest)
    this.props.updateDisplayedJob(id)
  }

  render() {
    let { listings, openJob } = this.props
    if (this.state.saved) listings = listings.filter(x => x.applied)
    const { page, saved } = this.state
    const pages = Array(Math.floor(listings.length/12) + (listings.length%12 > 0 ? 1 : 0)).fill(0).map((x,i) => i+1)
    return (
      <div className="App">
        <div className="filters">
          <div className="filter_label">Search: </div>
          <SearchBar
            onSearchTermChange={this.updateSearch}
          />
          <div className="applied">
            <div className="applied_title">Only saved jobs: </div>
            <i
              className={`fa fa-${saved ? 'check-' : ''}square-o fa-2x`}
              onClick={() => { this.toggleSaved() }}
              aria-hidden="true">
            </i>
          </div>
          <div className="app_title">{`CRAIG'S LIST JOBS (TECH, NATION-WIDE)`}</div>
        </div>
        <div className="app_body">
          {listings.length === 0 &&<div className="empty">There were no results for the search terms</div>}
          <div className = "listings_holder">
            <DropDown
              id="pages"
              title="Page"
              currentSelection={this.state.page}
              updateFunction={this.selectPage}
              dropdowns={pages}
            />
            {listings.slice((page-1)*12,page*12).map(l => Listing(l,this.updateListing))}
          </div>
          {Posting(openJob,this.markApplied)}
        </div>
      </div>
    )
  }
}
function mapStateToProps(state, ownProps, terms) {
  const { openJob } = state
  return { listings: ListingsSelector(state), openJob }
}

export default connect(mapStateToProps,{updateDisplayedJob, updateJobListings, updatePreferences})(App)
