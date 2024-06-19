#!/usr/bin/node
if (process.argv.length === 2) {
  console.log('Not a number');
} else if (isNaN(process.argv[2])) {
  console.log('Not a number');
} else {
  console.log(`My number: ${process.argv[2]}`);
}
