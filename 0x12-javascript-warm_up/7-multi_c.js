#!/usr/bin/node
// scrript that prints x times "C is fun"
// x is the first argument of the script

const argument = process.argv[2];

if (!isNaN(argument)) {
  const x = parseInt(argument);
  if (!isNaN(x)) {
    for (let i = 0; i < x; i++) {
      console.log('C is fun');
    }
  } else {
    console.log('Missing number of occurrences');
  }
} else {
  console.log('Missing number of occurrences');
}
