#!/usr/bin/node
/* Computes and prints a factorial of a number */
function factorial (num) {
  if (isNaN(num) || num <= 1) {
    return 1;
  }
  return (num * factorial(num - 1));
}
const { argv } = require('node:process');
console.log(factorial(parseInt(argv[2])));
