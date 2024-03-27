#!/usr/bin/node
const req = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];
req(url, function (error, response, body) {
  if (!error) {
    const charac = JSON.parse(body).characters;
    printCharacters(charac, 0);
  }
});

function printCharacters (charac, index) {
  req(charac[index], function (error, response, body) {
    if (!error) {
      console.log(JSON.parse(body).name);
      if (index + 1 < charac.length) {
        printCharacters(charac, index + 1);
      }
    }
  });
}
