#!/usr/bin/node

const square = require('./5-square');

class Square extends square {
  charPrint (c) {
    let character;
    if (c === undefined) {
      character = 'X';
    } else {
      character = c;
    }
    let i = this.width;
    while (i > 0) {
      let lineRow = '';
      for (let j = 0; j < this.width; j++) {
        lineRow += character;
      }
      console.log(lineRow);
      i--;
    }
  }
}
module.exports = Square;
