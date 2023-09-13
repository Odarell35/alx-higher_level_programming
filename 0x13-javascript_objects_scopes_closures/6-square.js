#!~/usr/bin/node
const Square1 = require('./5-square.js');
module.exports = class Square extends Square1 {
  charPrint (c) {
    if (c !== undefined) {
      let a = '';
      for (let i = 0; i < this.width; i++) {
        a = a + c;
      }
      for (let i = 0; i < this.height; i++) {
        console.log(a);
      }
    } else { return this.print(); }
  }
};
