#!/usr/bin/node
const args = process.argv.length;
let i;
if (args === 2) {
  console.log('No argument');
} else {
  for (i = 0; i < process.argv[2]; i++) {
    console.log('C is fun');
  }
}
