#!/usr/bin/node
/* Prints a message depending on the number of arguments */
const { argv } = require('node:process');
const argc = argv.length;
if (argc === 3) console.log('Argument found');
else if (argc > 3) console.log('Arguments found');
else console.log('No argument');
