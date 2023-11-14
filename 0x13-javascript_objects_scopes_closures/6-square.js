#!/usr/bin/node

const S1 = require('./5-square');
class Square extends S1 {
	charPrint(c) {
		let squ ='';
		for (let i = 0; i < this.width; i++)
		{
			if (c == 'C')
			{
				squ = squ + 'C';
			}
			else {
				squ = squ + 'X';
			}
		}
		for (let i = 0; i < this.height; i++)
		{
			console.log(squ);
		}
	}
}
module.exports = Square