#!/usr/bin/node

const dict = require('./101-data').dict;
const newDict = {};
let key = Object.keys(dict)[0];
while (key) {
  if (dict[key] in newDict) {
    newDict[dict[key]].push(key);
  } else {
    newDict[dict[key]] = [key];
  }
  key = Object.keys(dict)[Object.keys(dict).indexOf(key) + 1];
}
console.log(newDict);
