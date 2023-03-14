#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    this.width = (w > 0 && h > 0) ? w : undefined;
    this.height = (w > 0 && h > 0) ? h : undefined;
  }
}
module.exports = Rectangle;
