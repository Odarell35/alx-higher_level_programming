#!/usr/bin/node
const list = require('./100-data').list;
let j = 0;
const mapped = list.map(x => x * j++);
console.log(list);
console.log(mapped);
