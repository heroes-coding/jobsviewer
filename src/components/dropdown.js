import React from 'react'

function DropdownItem(props) {
  const { id, name, updateFunction, dropdownClass } = props
  const dClass = `dropdown-item ${dropdownClass || ''}`
  return (
    <button
      className={dClass}
      type="button"
      key={id}
      onClick={(event) => {
        event.preventDefault()
        updateFunction(name)
      }}
    >
      {name}
    </button>
  )
}

function renderButtonLabel(props) {
  if (props.buttonLabel) {
    return <span>{props.buttonLabel}&nbsp;&nbsp;</span>
  }
  return (
    <span className={props.textClass}>
      {props.name}{props.currentSelection}&nbsp;&nbsp;
    </span>
  )
}

export default (props) => {
  const {id, title, currentSelection, updateFunction, dropdownClass} = props
  return (
    <div className='dropdown_holder'>
      <button
        className='dropdown_main_button'
        id={id}
        data-toggle="dropdown"
        aria-haspopup="true"
        aria-expanded="false"
        title={title}
        onClick={(event) => { event.preventDefault() }}
      >
        <span className="dropdown_title">{title}: {currentSelection}</span>
        <span className="iconOnButton"><i className="fa fa-chevron-circle-down" aria-hidden="true"></i></span>
      </button>
      <div className="dropdown-menu" aria-labelledby={id}>
        {props.dropdowns.map((d,i) => {
          return (
            <DropdownItem
              key={i}
              id={i}
              name={d}
              updateFunction={updateFunction}
              dropdownClass={dropdownClass}
            />
          )
        })}
      </div>
    </div>
  )
}
