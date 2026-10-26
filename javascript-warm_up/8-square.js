#!/usr/bin/node
const x = parseInt(process.argv[2]);
let liste = '';
if (isNaN(x)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < x; i++) {
    liste += 'X';
  }
  for (let i = 0; i < x; i++) {
    console.log(liste);
  }
}
