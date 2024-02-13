#!/usr/bin/node
const dict = require('./101-data').dict;

const tlist = Object.entries(dict);
const v = Object.values(dict);
const valsUniq = [...new Set(v)];
const newDict = {};
for (const a in valsUniq) {
  const list = [];
  for (const b in tlist) {
    if (tlist[b][1] === valsUniq[a]) {
      list.unshift(tlist[b][0]);
    }
  }
  newDict[valsUniq[b]] = list;
}
console.log(newDict);
