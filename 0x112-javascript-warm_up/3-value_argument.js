#!/usr/bin/node
const args = process.argv;
if (process.argv[2] !== undefined) {
  console.log(args[2]);
} else {
  console.log('No argument');
}
