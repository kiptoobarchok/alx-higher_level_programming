#!/usr/bin/node

const arg = process.argv[2];

const num = parseInt(arg, 10);

if (isNaN(num)) {
  console.log('Missing number of occurences');
} else {
  for (let i = 0; i < num; i++) {
    console.log('C is fun');
  }
}
