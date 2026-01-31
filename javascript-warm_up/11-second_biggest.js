#!/usr/bin/node

const args = process.argv.slice(2).map(x => parseInt(x));

if (args.length < 2) {
  console.log(0);
} else {
  let max = Math.max(...args);
  const filtered = args.filter(n => n !== max);
  console.log(Math.max(...filtered));
}
