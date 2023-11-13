#!/usr/bin/node

function second_biggest (arr) {
  const intArray = arr.map(Number); // Convert the arguments to an array of integers

  if (intArray.length < 2) {
    console.log(0);
    return;
  }
  const sortedArray = intArray.sort((a, b) => b - a); // Sort the integers in descending order
  const secondLargest = sortedArray[1]; // Get the second element (second largest)

  console.log(secondLargest);
}

const args = process.argv.slice(2);
second_biggest(args);
