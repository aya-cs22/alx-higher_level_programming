#!/usr/bin/node
const args = process.argv;
if (process.argv[2]) {
  console.log(`${args[2]} is undefined`);
} else if (process.argv[3]) {
  console.log(`${args[3]} is cool`);
} else {
  console.log('undefined is undefined');
}
