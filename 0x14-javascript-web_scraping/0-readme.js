#!/usr/bin/node

const fs = require('fs');

const filePath = process.argv[2];

// Read the file content
fs.readFile(filePath, 'utf-8', function (err, data) {
  if (err) {
    console.log(err);
  } else {
    console.log(data);
  }
});
