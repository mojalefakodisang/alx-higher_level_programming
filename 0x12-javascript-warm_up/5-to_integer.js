#!/usr/bin/node
/* prints My number: <first argument converted in integer> if the first argument can be converted to an integer */
const { argv } = require('node:process');
function isInt (val) { return !isNaN(parseInt(val)); }
let msg = '';
if (isInt(argv[2])) msg = `My number: ${parseInt(argv[2])}`;
else msg = 'Not a number';
console.log(msg);
