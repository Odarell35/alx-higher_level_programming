#!/usr/bin/node
const x = process.argv[2];
const parsedx = parseInt(x, 10);
let k = '';
if (!isNaN(parsedx)) {
  for (let i = 0; i < x; i++) {
    k = k + 'X';
  } for (let i = 0; i < x; i++) {
    console.log(k);
  }
} else {
  console.log('Missing size');
}
