#!/usr/bin/node
/* Defines a class Square inherited from class Rectangle */
const Rectangle = require('./4-rectangle');
class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }
}
module.exports = Square;
