#!/usr/bin/node
/* Adds two integers */
function add (a, b) {
  console.log(parseInt(a) + parseInt(b));
}
const { argv } = require('node:process');
add(argv[2], argv[3]);
