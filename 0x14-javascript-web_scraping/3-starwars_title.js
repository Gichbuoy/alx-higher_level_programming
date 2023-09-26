#!/usr/bin/node

const request = require('request');

const epNumber = process.argv[2];

const API = 'https://swapi-api.hbtn.io/api/films/';

request(API + epNumber, function (error, response, body) {
  if (error) {
    console.log(error);
  } else if (response.statusCode === 200) {
    const responseJSON = JSON.parse(body);
    console.log(responseJSON.title);
  } else {
    console.log('Error code: ' + response.statusCode);
  }
});
