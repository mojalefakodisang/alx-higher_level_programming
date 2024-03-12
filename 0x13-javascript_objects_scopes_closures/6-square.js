#!/usr/bin/node
/* Defines a class Square inherited from class Rectangle */
const Rectangle = require('./5-square');
class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }

    for (let y = 0; y < this.width; y++) {
      console.log(`${c}`.repeat(this.width));
    }
  }
}
module.exports = Square;
