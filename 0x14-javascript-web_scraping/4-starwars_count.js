#!/usr/bin/node

const request = require('request');

const apiUrl = process.argv[2];

// Check if an API URL is provided as an argument
if (!apiUrl) {
  console.error('Please provide an API URL as an argument.');
  process.exit(1);
}

// Character ID for Wedge Antilles
const characterId = 18;

// Make a GET request to the Star Wars API films endpoint
request(apiUrl, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
    return;
  }

  // Check if the response status code is 200 (OK)
  if (response.statusCode !== 200) {
    console.error(`Error: Status Code ${response.statusCode}`);
    return;
  }

  const filmsData = JSON.parse(body);

  // Filter films where Wedge Antilles is present
  const filmsWithWedge = filmsData.results.filter(film => film.characters.includes(`https://swapi-api.alx-tools.com/api/people/${characterId}/`));

  console.log(`Number of movies with Wedge Antilles: ${filmsWithWedge.length}`);
});
