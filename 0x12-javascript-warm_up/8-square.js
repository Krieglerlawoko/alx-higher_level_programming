#!/usr/bin/node
if (isNaN(process.argv[2]) || process.argv[2] === undefined)) {
  console.log('Missing size');
} else {
  const a = Number(process.argv[2]);
  let i = 0;
  while (i < a) {
    console.log('X'.repeat(a));
    i++;
  }
}
