#!/usr/bin/node
const a = require('fs');
a.readFile(process.argv[2], 'utf8', function (error, content) {
  console.log(error || content);
});
