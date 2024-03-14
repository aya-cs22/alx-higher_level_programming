#!/usr/bin/node
const args = process.argv;
if (args === 2) {
  console.log('undefined is undefined');
} else if (args === 3) {
  console.log(process.argv[3] + ' is undefined');
} else if (args === 4) {
  console.log(process.argv[3] + ' is' + process.argv[3]);
}
