#!/usr/bin/node
/* Prints second biggest number */
const { argv } = require('node:process');
let temp;
let first;
let sec = 0;
if (argv.length > 1) {
  first = parseInt(argv[2]);
  sec = parseInt(argv[3]);
  if (sec > first) {
    temp = first;
    first = sec;
    sec = temp;
  }
  for (const i in argv) {
    if (parseInt(argv[i]) > first) {
      sec = first;
      first = parseInt(argv[i]);
    }
    if (parseInt(argv[i]) !== first && parseInt(argv[i]) > sec) {
      sec = parseInt(argv[i]);
    }
  }
}
console.log(sec);
