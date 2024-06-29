#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
const characterID = 18;
const characterURL = `https://swapi-api.alx-tools.com/api/people/${characterID}/`;

request(url, function (error, response, body) {
  if (error) {
    console.error(error);
    return;
  }
  if (response.statusCode !== 200) {
    console.log('Error: ' + response.statusCode);
    return;
  }

  const films = JSON.parse(body).results;
  let count = 0;

  films.forEach(film => {
    if (film.characters.includes(characterURL)) {
      count++;
    }
  });

  console.log(count);
});

// #!/usr/bin/node
// const request = require('request');
// const url = process.argv[2];
// const characterID = 18;
// const characterURL = `https://swapi-api.alx-tools.com/api/people/${characterID}/`;
// request(url, function (error, response, body) {
//   if (error) {
//     console.error(error);
//   } else if (response.statusCode !== 200) {
//     console.log(response.statusCode);
//   } else {
//     const films = JSON.parse(body).results;
//     let count = 0;
//     films.forEach(film => {
//       film.characters.forEach(character => {
//         if (film.characters.includes(characterURL)) {
//           count++;
//         }
//       });
//     });
//     console.log(count);
//   }
// });
