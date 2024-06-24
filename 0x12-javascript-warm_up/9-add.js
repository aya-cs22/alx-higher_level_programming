#!/usr/bin/node
if (process.argv.length === 2 || isNaN(parseInt(process.argv[2]))) {
  console.log('NaN');
} else {
  const num1 = parseInt(process.argv[2]);
  const num2 = parseInt(process.argv[3]);
  console.log(num1 + num2);
}
