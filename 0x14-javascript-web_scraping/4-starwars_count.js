#!/usr/bin/node

const request = require('request');
const apiUrl = process.argv[2];
const characterId = '18'; // Wedge Antilles' character ID

request(apiUrl, function (error, response, body) {
  if (error) {
    console.error(error);
    return;
  }

  const filmsData = JSON.parse(body).results;
  const moviesWithWedgeAntilles = filmsData.filter(film =>
    film.characters.includes(`https://swapi-api.alx-tools.com/api/people/${characterId}/`)
  );

  console.log(`Number of movies where Wedge Antilles is present: ${moviesWithWedgeAntilles.length}`);
});
