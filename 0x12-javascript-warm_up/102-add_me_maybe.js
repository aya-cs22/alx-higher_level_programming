#!/usr/bin/node
exports.addMeMaybe = function addMeMaybe (number, theFunction) {
  number++;
  return theFunction(number);
};
