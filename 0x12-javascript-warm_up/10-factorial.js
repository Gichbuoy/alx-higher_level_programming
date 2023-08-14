#!/usr/bin/node
// script that computes and prints a factorial

function factorial (n) {
  if (isNaN(n)) {
    return 1;
  } else if (n === 0) {
    return 1;
  } else {
    return n * factorial(n - 1);
  }
}

const argument = process.argv[2];
const num = parseInt(argument);

const result = factorial(num);
console.log(result);
