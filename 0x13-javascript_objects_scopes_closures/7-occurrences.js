#!/usr/bin/node
// function that returns the number of occurrences in a list.

exports.nbOccurences = function (list, searchElement) {
  let numOccurences = 0;
  for (let x = 0; x < list.length; x++) {
    if (searchElement === list[x]) {
      numOccurences++;
    }
  }
  return numOccurences;
};
