#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  let c = 0;
  list.forEach(element => {
    if (element === searchElement) {
      c++;
    }
  });
  return c;
};
