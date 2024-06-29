#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
const characterID = 18;

request(url, function (error, response, body) {
  if (error) {
    console.error(error);
  }
  if (response.statusCode !== 200) {
    console.log(response.statusCode);
  }

  const films = JSON.parse(body).results;
  let count = 0;

  films.forEach(film => {
    film.characters.forEach(character => {
      if (character.endsWith(`/${characterID}/`)) {
        count++;
      }
    });
  });

  console.log(count);
});
