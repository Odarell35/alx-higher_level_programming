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
	console.log(filmsData.reduce(count, movie) => {
		return movie.characters.find((character) => character.endsWith('/18/'))
		? count + 1
		: count;
	}, 0);

});
