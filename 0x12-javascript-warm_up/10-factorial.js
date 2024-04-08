#!/usr/bin/node
const args = process.argv;
const n = parseInt(args[2]);
function factorial (n) {
  if (isNaN(n)) {
    return NaN;
  } else if (n === 0 || n === 1) {
    return 1;
  } else {
    return n * factorial(n - 1);
  }
}

console.log(factorial(n));
