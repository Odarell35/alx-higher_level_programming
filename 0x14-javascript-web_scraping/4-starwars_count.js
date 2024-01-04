#!/usr/bin/node

const request = require('request');
const apiUrl = process.argv[2];
let c = 0;

request(apiUrl, function (error, response, body) {
  if (error) {
    console.error(error);
    return;
  }

  const filmsData = JSON.parse(body).results;
  filmsData.forEach((film) => {
    film.characters.forEah((character) => {
      if (character.includes('18')) {
        c += 1;
      }
    });
  });
  console.log(c);
});
