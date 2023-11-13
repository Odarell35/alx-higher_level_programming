#!/usr/bin/node

const first = process.argv[2];
const parsedInt = parseInt(first, 10);
if (!isNaN(parsedInt)) {
  console.log(`My number: ${parsedInt}`);
} else {
  console.log('Not a number');
}
