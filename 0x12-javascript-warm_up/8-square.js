#!/usr/bin/node
const args = process.argv.length;
let i;
if (args === 2) {
  console.log('Missing size');
} else {
  for (i = 0; i < process.argv[2]; i++) {
    console.log('X'.repeat(process.argv[2]));
  }
}
