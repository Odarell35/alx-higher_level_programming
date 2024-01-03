#!/usr/bin/node

const request = require('request');
const movieid = process.argv[2];
const url = 'https://swapi-api.alx-tools.com/api/films/';

request(url + movieid, function (error, response, body) {
  if (error) {
    console.error(error);
    return;
  }
  const responseJSON = JSON.parse(body);
  console.log(responseJSON.title);
});
