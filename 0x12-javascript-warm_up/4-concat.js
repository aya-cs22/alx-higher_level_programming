#!/usr/bin/node
const args = process.argv;
if (args.length === 2) {
  console.log('undefined is undefined');
} else if (args.length === 3) {
  console.log(`${args[2]} is undefined`);
} else {
  console.log(`${args[2]} is cool`);
}
// c cool
// c is cool

// c
// c is undefined

// undefined is undefined
