#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let i = 0;
    let lineRow = '';

    while (i < this.width) {
      lineRow += 'X';
      i++;
    }
    i = 0;

    while (i < this.height) {
      console.log(lineRow);
      i++;
    }
  }
}
module.exports = Rectangle;
