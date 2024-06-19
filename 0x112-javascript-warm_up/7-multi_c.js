#!/usr/bin/node
const args = process.argv;
let i;
if (args.length === 2) {
  console.log('Missing number of occurrences');
} else if (args.length === 3) {
  for (i = 0; i < args[2]; i++) {
    console.log('C is fun');
  }
}
