#!/usr/bin/node
function addMeMaybe(number, theFunction){
    number++;
    theFunction(number);
};
module.export.addMeMaybe = addMeMaybe;
