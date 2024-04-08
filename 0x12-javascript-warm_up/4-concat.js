#!/usr/bin/node
const args = process.argv;
if (process.argv[3]) {
  console.log(`${args[2]} is ${args[3]}`);
} else if (process.argv[2]) {
  console.log(`${args[2]} is undefined`);
} else {
  console.log('undefined is undefined');
}
