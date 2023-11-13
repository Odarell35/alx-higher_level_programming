#!/usr/bin/node

let i = 0;
let arguments = process.argv
arguments.forEach((val, index) => {
  i++;
  if (index === 2) { console.log(`${val}`); }
});
if (i <= 2) {
  console.log('No argument');
}
