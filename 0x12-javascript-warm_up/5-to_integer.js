#!/usr/bin/node

const args = process.argv[2];

console.log(isNaN(parseInt(args)) ? 'Not a number' : 'My number: ' + parseInt(args));
