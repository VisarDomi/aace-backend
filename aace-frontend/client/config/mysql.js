// MYSQL SETUP

const
  mysql = require('mysql'),
  hl = require('handy-log'),
  { MYSQL_HOST, MYSQL_USER, MYSQL_PASSWORD, MYSQL_DATABASE } = process.env

// CREATES A DB CONNECTION
const db = mysql.createConnection({
  host:     'localhost',
  user:     'root',
  password: 'mysqlpassword',
  database: 'vuetut',
  charset:  'utf8mb4'
})

// CONNECTS DB
db.connect(err => {
  if(err){
    hl.error(err)
  }
})

module.exports = db
