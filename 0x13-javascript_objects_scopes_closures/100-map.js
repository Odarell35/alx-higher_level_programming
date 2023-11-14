#!/usr/bin/node
const list = require('./100-data').list;
let j = 0;
const map_list = list.map(x => x * j++);
console.log(list);
console.log(map_list);