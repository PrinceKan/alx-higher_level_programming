#!/usr/bin/node

const n = Number(process.argv[2]);

function fact (n) {
  let result = 1;
  for (let i = 1; i <= n; i++) {
    result *= i;
  }
  return result;
}
if (isNaN(n)) {
  console.log(1);
} else {
  console.log(fact(n));
}
