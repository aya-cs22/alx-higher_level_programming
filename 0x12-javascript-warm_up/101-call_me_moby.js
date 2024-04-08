#!/usr/bin/node
let i;
function callMeMoby (x, theFunction) {
  for (i = 0; i < x; i++) {
    theFunction();
  }
}
exports.callMeMoby = callMeMoby;
