#!/usr/bin/node

const httpRequest = require('request');

const movieId = process.argv[2] + '/';
const movieApiUrl = 'https://swapi-api.hbtn.io/api/films/';

httpRequest(movieApiUrl + movieId, async function (error, response, responseBody) {
  if (error) return console.error(error);

  const characterUrlList = JSON.parse(responseBody).characters;

  for (const characterUrl of characterUrlList) {
    await new Promise(function (resolve, reject) {
      httpRequest(characterUrl, function (error, response, responseBody) {
        if (error) return console.error(error);

        console.log(JSON.parse(responseBody).name);
        resolve();
      });
    });
  }
});