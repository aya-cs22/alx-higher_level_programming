#!/usr/bin/node
const args = process.argv;
if (args.length === 2 || args.length === 3) {
  console.log('NaN');
} else {
  const num1 = parseFloat(process.argv[2]);
  const num2 = parseFloat(process.argv[3]);
  if (isNaN(num1) || isNaN(num2)) {
    console.log('NaN');
  } else {
    console.log(num1 + num2);
  }
}
