#!/usr/bin/node
const process = require('process');
const request = require('request');
const movieId = process.argv[2];
const url = 'https://swapi-api.alx-tools.com/api/films/';
const movieUrl = url + movieId;
request(movieUrl, (error, response, body) => {
	if (!error) {
		content = JSON.parse(body);
		console.log(content.title);
	}
});
