#!/usr/bin/node

function factorialize (number) {
  let results = 1;
  for (let i = 1; i <= number; i++) {
    results = results * i;
  }
  return (results);
}
console.log(factorialize(parseInt(process.argv[2])));
