#!/usr/bin/node

const argument = process.argv;
const length = argument.length;

if (length === 2) {
  console.log('No argument');
}
if (length === 3) {
  console.log('Argument found');
}
if (length > 3) {
  console.log('Arguments found');
}
