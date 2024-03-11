#!/usr/bin/node
/* Prints x times 'C is fun' */
const { argv } = require('node:process');
const count = parseInt(argv[2]);
if (argv[2] === undefined) console.log('Missing number of occurences');
for (let i = 0; i < count; i++) console.log('C is fun');
