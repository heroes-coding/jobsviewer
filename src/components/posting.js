import React from 'react'

const Posting = (openJob, markApplied) => {
  if (!openJob) return <div className = "job_details"></div>
  const { body, link, applied, id } = openJob
  return (
    <div className = "job_details">
      <div className="external_link">
      <div className="link_title">Click to open link: </div>
        <i
          className="fa fa-external-link fa-2x"
          onClick={() => {
            Object.assign(document.createElement('a'), { target: '_blank', href: link}).click();
          }}
          aria-hidden="true">
        </i>
      </div>
      <div className="applied">
        <div className="applied_title">Applied to position: </div>
        <i
          className={`fa fa-${applied ? 'check-' : ''}square-o fa-2x`}
          onClick={() => {
            console.log({id,applied})
            markApplied(id,!applied)
          }}
          aria-hidden="true">
        </i>
      </div>
      {openJob && <div dangerouslySetInnerHTML={{__html:body}} />}
    </div>

  )
}

export default Posting
