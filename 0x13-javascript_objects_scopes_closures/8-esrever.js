#!/usr/bin/node
/* Reverses a list */
exports.esrever = function (list) {
  const reversed = [];
  if (list === undefined || list.length === 0) return [];
  for (let i = list.length - 1; i >= 0; i--) {
    reversed.push(list[i]);
  }
  return reversed;
};
