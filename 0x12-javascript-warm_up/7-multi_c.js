#!/usr/bin/node

const numberOfOccurence = parseInt(process.argv[2]);

let i = 0;

if (numberOfOccurence && !isNaN(numberOfOccurence)) {
  while (i < numberOfOccurence) {
    console.log('C is fun');
    i++;
  }
} else {
  console.log('Missing number of occurrences');
}
