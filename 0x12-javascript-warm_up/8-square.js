#!/usr/bin/node
// script that prints a square

const argument = process.argv[2];

if (!isNaN(argument)) {
  const size = parseInt(argument);
  if (!isNaN(size)) {
    for (let i = 0; i < size; i++) {
      let row = '';
      for (let j = 0; j < size; j++) {
        row += 'X';
      }
      console.log(row);
    }
  } else {
    console.log('Missing size');
  }
} else {
  console.log('Missing size');
}
