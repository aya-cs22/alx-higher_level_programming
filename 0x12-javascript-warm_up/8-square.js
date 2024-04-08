#!/usr/bin/node
const args = process.argv;
let i, x;
if (args.length === 2) {
  console.log('Missing size');
} else if (args.length === 3) {
  for (i = 0; i < args[2]; i++) {
    let row = '';
    for (x = 0; x < args[2]; x++) {
      row += 'X';
    }
    console.log(row);
  }
}
