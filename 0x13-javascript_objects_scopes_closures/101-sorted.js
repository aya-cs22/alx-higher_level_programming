#!/usr/bin/node

const { dict } = require('./101-data');

for (const key in dict) {
  if (Object.prototype.hasOwnProperty.call(dict, key)) {
    console.log(`Key: ${key}, Value: ${dict[key]}`);
  }
}
