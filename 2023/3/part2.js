const { createInterface } = require("readline");

async function main() {
  const symbols = {};
  const numbers = [];
  let i = 0;
  for await ( line of createInterface({ input: process.stdin }) ) {
    let j = 0;
    let last_was_digit = false
    let number = {
      value: 0,
      coordinates: [],
    }
    for (const c of line) { 
      d = Number.parseInt(c);
      if ( !isNaN(d) ) {
        number.value = number.value * 10 + d; 
        number.coordinates.push([j, i]);
        last_was_digit = true;
      } else if (c === '*') {
        symbols[[j, i].toString()] = [];
        if (last_was_digit) {
          numbers.push(number);
          number = { 
            value: 0,
            coordinates: [],
            ratio: []
          }
          last_was_digit = false;
        }
      } else {
        if (last_was_digit) {
          numbers.push(number);
          number = { 
            value: 0,
            coordinates: [],
            ratio: []  
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
        coordinates: [],
        ratio: []
      }
      last_was_digit = false;
    }
    i++;
  }

  for ( n of numbers ) {
    updateAdjacent(n, symbols);
  }

  let total = 0;
  for ( const s of Object.values(symbols) ) {
    if (s.length === 2) {
      total += s[0] * s[1];
    }
  }
  console.log(total);
}

function updateAdjacent(numberEntry, symbolCoords) {
  const visited = new Set();
  numberEntry.coordinates.forEach(([x, y]) => {
    const adjacentCoords = [
        [x - 1, y - 1].toString(),
        [x, y - 1].toString(),
        [x + 1, y - 1].toString(),
        [x - 1, y].toString(),
        [x + 1, y].toString(),
        [x - 1, y + 1].toString(),
        [x, y + 1].toString(),
        [x + 1, y + 1].toString()
    ]
    for ( const coords of adjacentCoords ) {
      if ( coords in symbolCoords && !visited.has(coords)) {
        symbolCoords[coords].push(numberEntry.value)
      }
      visited.add(coords);
    }
  });
}

if (require.main === module) {
  main()
}
