#!/usr/bin/node
if (process.argv.length === 2 || isNaN(parseInt(process.argv[2]))) {
  console.log('Missing number of occurrences');
} else {
  const num = parseInt(process.argv[2]);
  for (let i = 0; i < num; i++) {
    console.log('C is fun');
  }
}
