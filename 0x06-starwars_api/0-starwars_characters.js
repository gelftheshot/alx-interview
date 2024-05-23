#!/usr/bin/node

const httpRequest = require('request');

const movieId = process.argv[2] + '/';
const movieApiUrl = 'https://swapi-api.hbtn.io/api/films/';

httpRequest(movieApiUrl + movieId, async function (error, response, responseBody) {
  if (error) {
    console.error(error);
    return;
  }

  const characterUrlList = JSON.parse(responseBody).characters;

  for (const characterUrl of characterUrlList) {
    await new Promise(function (resolve, reject) {
      httpRequest(characterUrl, function (error, response, responseBody) {
        if (error) {
          console.error(error);
          return reject(error);
        }

        console.log(JSON.parse(responseBody).name);
        resolve();
      });
    }).catch((error) => {
      console.error(error);
    });
  }
});