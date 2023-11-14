#!/usr/bin/node

class Rectangle {
	constructor(w, h) {
		if (w > 0 && h > 0) {
			this.width = w;
			this.height = h;
		}
		}
	print() {
		let rect = '';
		for (let i = 0; i < this.width; i++){
			rect = rect + 'X';
			}
		for (let i = 0; i < this.height; i++) {
			console.log(rect);
			}
	}

	rotate () {
		let x = this.height;
		this.height = this.width;
		this.width = x;
	}
	double () {
		this.width = this. width * 2;
		this.height = this.height * 2;
	}
}
module.exports = Rectangle