#!/usr/bin/node
const args = process.argv;
if (args.length === 2) {
  console.log('Not a number');
} else if (args.length === 3) {
  if (isNaN(Number)) {
    console.log('Not a number');
  } else {
    const integer = Math.floor(args[2]);
    console.log('My number: ' + integer);
  }
}
