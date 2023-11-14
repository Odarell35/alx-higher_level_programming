#!/usr/bin/node

exports.converter = function (base) {
  function convtobase (number) {
    return number.toString(base);
  }
  return convtobase;
};
