#!/usr/bin/node

if (process.argv.length <= 3) {
  console.log(0);
} else {
  const list = process.argv.slice(2).map(Number);
  let m = 0;

  for (let i = 0; i < list.length; i++) {
    if (list[i] > m) {
      m = list[i];
    }
  }

  let secondMax = 0;

  for (let j = 0; j < list.length; j++) {
    if (list[j] > secondMax && list[j] !== m) {
      secondMax = list[j];
    }
  }
  console.log(secondMax);
}
