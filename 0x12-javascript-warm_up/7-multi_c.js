#!/usr/bin/node
if (isNaN(process.argv[2]) || process.argv[2] === undefined)) {
  console.log('Missing number of occurrences');
} else {
  const a = Number(process.argv[2]);
  let k = 0;
  while (k < a) {
    console.log('C is fun');
    k++;
  }
}
