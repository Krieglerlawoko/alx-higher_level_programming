#!/usr/bin/node
const a = require('fs');
a.writeFile(process.argv[2], process.argv[3], error => {
  if (error) console.log(error);
});
