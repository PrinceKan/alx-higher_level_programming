#!/usr/bin/node

const sizeOfSquare = parseInt(process.argv[2]);

if (isNaN(sizeOfSquare)) {
  console.log('Missing size');
} else {
  let i = 0;
  let square = '';
  while (i < sizeOfSquare) {
    square += 'X';
    i++;
  }
  i = 0;
  while (i < sizeOfSquare) {
    console.log(square);
    i++;
  }
}
