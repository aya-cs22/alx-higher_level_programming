#!/usr/bin/node

const request = require('request');
const URL = process.argv[2];
const file = process.argv[3];

request(URL, (error, response, body) => {
  if (!error) {
    const fs = require('fs');
    fs.writeFileSync(file, body, 'utf8');
  }
});
