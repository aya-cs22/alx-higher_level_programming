#!/usr/bin/node
const args = process.argv;
if (args.length === 2) {
  console.log('undefined is undefined');
} else if (args.length === 3) {
  console.log(process.argv[2] + ' is undefined');
} else if (args.length === 4) {
  console.log(process.argv[2] + ' is ' + process.argv[3]);
}
