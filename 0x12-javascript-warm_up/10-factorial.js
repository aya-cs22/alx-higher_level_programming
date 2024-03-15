#!/usr/bin/node
let factorial = 1;
let i;
const num1 = parseFloat(process.argv[2]);
if (num1 === 2) {
  console.log('Missing size');
} else {
  for (i = 1; i <= process.argv[2]; i++) {
    factorial *= i;
  }
  console.log(factorial);
}
