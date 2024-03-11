#!/usr/bin/node
/* Prints a square */
const { argv } = require('node:process');
const size = parseInt(argv[2]);
if (size === 'NaN' || argv[2] === undefined) {
  console.log('Missing size');
} else {
  for (let i = 0; i < size; i++) {
    console.log('X'.repeat(size));
  }
}
