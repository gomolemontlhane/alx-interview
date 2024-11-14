#!/usr/bin/node

const request = require('request');
const movieId = process.argv[2];

if (!movieId) {
  console.log('Usage: ./0-starwars_characters.js <movie_id>');
  process.exit(1);
}

// Star Wars API URL for films
const url = `https://swapi-api.hbtn.io/api/films/${movieId}`;

request(url, (error, response, body) => {
  if (error) {
    console.error('Error fetching data:', error);
    return;
  }

  // Parse response JSON
  const movieData = JSON.parse(body);
  const characters = movieData.characters;

  // Function to fetch and print character names in order
  const fetchCharacterName = (characterUrl) => {
    return new Promise((resolve, reject) => {
      request(characterUrl, (err, res, data) => {
        if (err) reject(err);
        else resolve(JSON.parse(data).name);
      });
    });
  };

  // Iterate and print character names in sequence
  (async () => {
    for (const characterUrl of characters) {
      try {
        const characterName = await fetchCharacterName(characterUrl);
        console.log(characterName);
      } catch (err) {
        console.error('Error fetching character name:', err);
      }
    }
  })();
});
