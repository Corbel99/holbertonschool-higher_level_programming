#!/usr/bin/node
if (process.argv[3] === undefined) {
  console.log(0);
} else {
  let first = -Infinity;
  let second = -Infinity;
  for (let i = 2; i < process.argv.length; i++) {
    const n = parseInt(process.argv[i]);
    if (n > first) {
      second = first;
      first = n;
    } else if (n > second) {
      second = n;
    }
  }
  console.log(second);
}
