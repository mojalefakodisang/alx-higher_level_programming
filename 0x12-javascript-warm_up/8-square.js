#!/usr/bin/node
/* Prints a square */
const { argv } = require('node:process');
const size = parseInt(argv[2]);
let msg = '';
if (size === 'NaN' || argv[2] === undefined) msg = 'Missing size';
for (let x = 0; x < size; x++) {
  for (let y = 0; y < size; y++) msg += 'X';
  if (x < size - 1) msg += '\n';
}
console.log(msg);
