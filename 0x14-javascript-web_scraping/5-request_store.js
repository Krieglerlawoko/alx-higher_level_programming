#!/usr/bin/node
const a = require('fs');
const req = require('request');
req(process.argv[2]).pipe(a.createWriteStream(process.argv[3]));
