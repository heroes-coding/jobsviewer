const fs = require('fs')
const path = require('path')
const SAVE_PATH = 'F:/apiFiles'
const PYTHON_3_PATH = 'c:/users/jeremy/miniconda/python'
const DB_CONFIG_PATH = path.join(SAVE_PATH,'dbConfig.json')

module.exports = {

  SAVE_PATH,
  DB_CONFIG_PATH,
  PYTHON_3_PATH,

}
