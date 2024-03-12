#!/usr/bin/node
/* Module that checks number of occurences of a number in a list */
exports.nbOccurences = function (list, searchElement) {
  let count = 0;
  if (list.length === 0 || list === undefined || searchElement === undefined) return 0;
  for (let i = 0; i < list.length; i++) {
    if (searchElement === list[i]) {
      count += 1;
    }
  }
  return count;
};
