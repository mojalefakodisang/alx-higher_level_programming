#!/usr/bin/node
/* Prints the number of arguments already printed */
const logs = [];
exports.logMe = function (item) {
  logs.push(item);
  for (let i = 0; i < logs.length; i++) {
    if (item === logs[i]) {
      console.log(`${i}: ${item}`);
    }
  }
};
