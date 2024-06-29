#!/usr/bin/node
const request = require('request');
const url = 'https://swapi-api.alx-tools.com/api/films/';
const characterID = 18;
request(url, function (error, response, body) {
  if (error) {
    console.error(error);
  } else if (response.statusCode !== 200) {
    console.log(response.statusCode);
  } else {
    const films = JSON.parse(body).results;
    let count = 0;
    films.forEach(film => {
      film.characters.forEach(character => {
        if (character.includes(`/api/people/${characterID}/`)) {
          count++;
        }
      });
    });
    console.log(count);
  }
});
