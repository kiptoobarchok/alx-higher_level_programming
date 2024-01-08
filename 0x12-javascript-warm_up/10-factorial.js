#!/usr/bin/node

function factorial (arg) {
  if (isNaN(arg) || arg <= 0 || arg === 1) {
    return 1;
  } else {
    return arg * factorial(arg - 1);
  }
}

const arg = parseInt(process.argv[2], 10);

const res = factorial(arg);
console.log(res);
