import React, { Component } from 'react'
import _ from 'lodash'

class SearchBar extends Component {
  constructor(props) {
    super(props)
    this.state = { term: '' }
    this.clearSearch = this.clearSearch.bind(this)
    this.search = this.search.bind(this)
  }
  clearSearch() {
    this.setState({term: ''})
  }
  componentWillUnmount() {
    if (this.clearTimeout) {
      clearTimeout(this.clearTimeout)
    }
  }
  search() {
    this.props.onSearchTermChange(this.state.term)
  }
  onInputChange(term) {
    this.setState({term})
    if (this.searchTimeout) clearTimeout(this.searchTimeout)
    this.searchTimeout = setTimeout(this.search, 500)
  }
  render() {
    return (
      <input
        id={this.props.id}
        placeholder={ this.props.placeholder }
        className={this.props.overClass || "searchInput"}
        value = { this.state.term }
        onChange={ event => { this.onInputChange(event.target.value) }}
        style={ this.props.style }
      />
    )
  }

}

export default SearchBar
