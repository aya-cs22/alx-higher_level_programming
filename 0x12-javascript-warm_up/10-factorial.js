#!/usr/bin/node
const args = process.argv;
const n = parseInt(args[2]);
function factorial (n) {
  if (n === 0 || n === 1) {
    return 1;
  } else {
    return n * factorial(n - 1);
  }
}
if (args.length < 3) {
  process.exit(1);
} else {
  console.log(factorial(n));
}
