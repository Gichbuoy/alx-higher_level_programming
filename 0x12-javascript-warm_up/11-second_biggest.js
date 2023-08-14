#!/usr/bin/node
// script that searches the 2nd biggest integer in list of args

function findSecondLargest (nums) {
  if (nums.length <= 1) {
    return 0;
  }

  let largest = -Infinity;
  let secondLargest = -Infinity;

  for (const num of nums) {
    const currentNum = parseInt(num);
    if (currentNum > largest) {
      secondLargest = largest;
      largest = currentNum;
    } else if (currentNum > secondLargest && currentNum !== largest) {
      secondLargest = currentNum;
    }
  }

  return secondLargest;
}

const argumentsList = process.argv.slice(2);
const secondLargest = findSecondLargest(argumentsList);
console.log(secondLargest);
