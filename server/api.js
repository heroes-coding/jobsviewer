const express = require('express')
const app = express()
const path = require('path')
const fs = require('fs')
const { DB_CONFIG_PATH, STATS_PATH } = require('../config')
const { createDatabase } = require('./postgresql')
// const { asleep } = require('../helpers/tinyHelpers')
const database = createDatabase(DB_CONFIG_PATH)

const bodyParser = require('body-parser')
app.use(bodyParser.json())
app.use(bodyParser.urlencoded({ extended: true }))

app.use(function(req, res, next) {
  // Website you wish to allow to connect
  res.setHeader('Access-Control-Allow-Origin', 'http://localhost:4101')
  // Request methods you wish to allow
  res.setHeader('Access-Control-Allow-Methods', 'GET, POST')
  // Request headers you wish to allow
  res.setHeader('Access-Control-Allow-Headers', 'X-Requested-With,content-type')
  // Set to true if you need the website to include cookies in the requests sent
  // to the API (e.g. in case you use sessions)
  res.setHeader('Access-Control-Allow-Credentials', true)
  // Pass to next layer of middleware
  next()
})

app.get('/body/:job', async function(req, res) {
  try {
    const query = "SELECT region, state, link, day, month, location, title, body, id, applied, timestamp FROM listings WHERE id = ($1);"
    const result = await database.simpleQuery(query,[req.params.job])
    if (result.rowCount) {
      res.send(result.rows)
    } else {
      return res.send({status:404})
    }
  } catch (e) {
    return res.send(e.message)
  }
})

app.get('/apply/:job_id', async function(req, res) {
  let [job_id,applied] = req.params.job_id.split(",")
  console.log(req.params.job_id)
  applied = applied === 'true' ? true : false
  try {
    const query = 'UPDATE listings SET applied = ($2) WHERE id = ($1)'
    const result = await database.simpleQuery(query,[job_id, applied])
    res.send("Got it!")
  } catch (e) {
    return res.send(e.message)
  }
})



app.get('/search/', async function(req, res) {
  try {
    const query = 'SELECT id,region, state, link, day, month, location, title, applied, timestamp FROM listings;'
    const result = await database.simpleQuery(query)
    if (result.rowCount) {
      res.send(result.rows)
    } else {
      return res.send([])
    }
  } catch (e) {
    return res.send(e.message)
  }
})

app.get('/search/:terms', async function(req, res) {
  const searchTerms = req.params.terms.split(',')
  console.log({searchTerms})
  try {
    const query = 'SELECT id,region, state, link, day, month, location, title, applied, timestamp FROM listings WHERE tokens @@ to_tsquery($1) and body is not null;'
    const result = await database.simpleQuery(query,[searchTerms.join(" & ")])
    if (result.rowCount) {
      res.send(result.rows)
    } else {
      return res.send([])
    }
  } catch (e) {
    return res.send(e.message)
  }
})


app.set('LOGIN_FAILURE',function(req, res) { res.status(500).send(res.error) })
app.listen(4100, () => console.log('Auth server listening on port 4100!'))
