#!/usr/bin/node
const fs = require('fs');

const fil1 = fs.readFileSync(process.argv[2]).toString();
const fil2 = fs.readFileSync(process.argv[3]).toString();
fs.writeFileSync(process.argv[4], fil1 + fil2);
