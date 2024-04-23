#!/usr/bin/node
const process = require('process');
const request = require('request');
const requestURL = process.argv[2];
request(requestURL, (error, response, body) => {
	if (!error) {
		console.log(`code: ${response.statusCode}`);
	}
});
