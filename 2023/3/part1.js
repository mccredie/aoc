const { createInterface } = require("readline");

async function main() {
  const symbols = new Set();
  const numbers = [];
  let i = 0;
  for await ( line of createInterface({ input: process.stdin }) ) {
    let j = 0;
    let last_was_digit = false
    let number = {
      value: 0,
      coordinates: []
    }
    for (const c of line) { 
      d = Number.parseInt(c);
      if ( !isNaN(d) ) {
        number.value = number.value * 10 + d; 
        number.coordinates.push([j, i]);
        last_was_digit = true;
      } else if (c !== '.') {
        symbols.add([j, i].toString());
        if (last_was_digit) {
          numbers.push(number);
          number = { 
            value: 0,
            coordinates: []
          }
          last_was_digit = false;
        }
      } else {
        if (last_was_digit) {
          numbers.push(number);
          number = { 
            value: 0,
            coordinates: []
          }
          last_was_digit = false;
        }
      }
      j++;
    }
    if (last_was_digit) {
      numbers.push(number);
      number = { 
        value: 0,
        coordinates: []
      }
      last_was_digit = false;
    }
    i++;
  }

  total = 0;
  for ( n of numbers ) {
    if (isAdjacentToAny(n, symbols)) {
      total += n.value;
    }
  }
  console.log(total);
}

function isAdjacentToAny(numberEntry, symbolCoords) {
  return numberEntry.coordinates.some(([x, y]) => (
      symbolCoords.has([x - 1, y - 1].toString()) ||
      symbolCoords.has([x, y - 1].toString()) ||
      symbolCoords.has([x + 1, y - 1].toString()) || 
      symbolCoords.has([x - 1, y].toString()) ||
      symbolCoords.has([x + 1, y].toString()) ||
      symbolCoords.has([x - 1, y + 1].toString()) ||
      symbolCoords.has([x, y + 1].toString()) ||
      symbolCoords.has([x + 1, y + 1].toString())
  ));
}

if (require.main === module) {
  main()
}
