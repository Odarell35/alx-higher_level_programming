#!/usr/bin/node
let argslen = process.argv.length;
if (argslen === 2)
{
	console.log('No argument');
}
if (argslen === 3)
{
	console.log('Argument found');
}
if (argslen > 3)
{
	console.log('Arguments found');
}
