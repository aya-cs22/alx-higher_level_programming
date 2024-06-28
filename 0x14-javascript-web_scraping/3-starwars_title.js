#!/usr/bin/node
const request = require('request');
const id = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${id}`;

request(url, function (error, response, body) {
  if (error) {
    console.error(error);
  } else if (response.statusCode !== 200) {
    console.log(response.statusCode);
  } else {
    const objBody = JSON.parse(body);
    console.log(objBody.title);
  }
});
