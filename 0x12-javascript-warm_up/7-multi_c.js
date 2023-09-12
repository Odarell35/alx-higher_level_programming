#!/usr/bin/node
const x = process.argv[2];
const parsedx = parseInt(x, 10);
if(!isNaN(parsedx)){
for (let i = 0; i < x; i++){
	console.log('C is fun');
}}
else {
	console.log('Missing number of occurrences');
}
