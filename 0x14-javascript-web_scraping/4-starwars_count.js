#!/usr/bin/node
const request = require('request');
const url = 'https://swapi-api.alx-tools.com/api/films/';
request(url, (error, response, body) => {
  if (!error) {
    const films = JSON.parse(body).results;
    let charCount = 0;
    for (const film of films) {
      if (film.characters.some(character => character.endsWith('/18/'))) {
        charCount++;
      }
    }
    console.log(charCount);
  }
});
