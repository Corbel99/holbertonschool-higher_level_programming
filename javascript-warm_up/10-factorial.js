#!/usr/bin/node
function factorial (n) {
  if (n <=1 || isNaN(n)) {
    return 1;
  } else {
    return n * factorial(n - 1);
  }
}
const result = factorial(process.argv[2]);
console.log(result);
