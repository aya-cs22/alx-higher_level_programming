#!/usr/bin/node
const args = process.argv;
if (args.length === 2) {
  console.log('NaN');
} else if (args.length === 3) {
  console.log('NaN');
} else {
  const num1 = parseInt(args[3]);
  const num2 = parseInt(args[4]);
  if (!isNaN(num1) && !isNaN(num2)) {
    console.log(num1 + num2);
  }
}
