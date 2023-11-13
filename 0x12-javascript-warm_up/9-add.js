#!/usr/bin/node
const a = process.argv[2];
const b = process.argv[3];
function add (a, b) {
  const parseda = parseInt(a);
  const parsedb = parseInt(b);
  console.log(parseda + parsedb);
}
add(a, b);
