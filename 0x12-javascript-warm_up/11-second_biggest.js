#!/usr/bin/node

const args = process.argv.slice(2);

if (args.length <= 1) {
  console.log(0);
} else {
  const sorted = args.map(arg => parseInt(arg, 10)).sort((a, b) => b - a);

  console.log(sorted[1]);
}
