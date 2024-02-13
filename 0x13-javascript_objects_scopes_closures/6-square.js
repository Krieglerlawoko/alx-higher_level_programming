#!/usr/bin/node
const SquareA = require('./5-square');

class Square extends SquareA {
  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }
    for (let a = 0; a < this.height; a++) {
      let k = '';
      for (let b = 0; b < this.width; b++) {
        k += c;
      }
      console.log(k);
    }
  }
}

module.exports = Square;
