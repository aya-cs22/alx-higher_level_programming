#!/usr/bin/node
const args = process.argv;
a = args[2];
b = args[3];
function add(a,b){
    return a+b;
}
exports.add = add;
