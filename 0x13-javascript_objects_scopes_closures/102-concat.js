#!/usr/bin/node
const fl = require('fs');
const firstFile = fl.readFileSync(process.argv[2], 'utf8');
const secondFile = fl.readFileSync(process.argv[3], 'utf8');
const newFile = firstFile + secondFile;
fl.appendFileSync(process.argv[4], newFile);
