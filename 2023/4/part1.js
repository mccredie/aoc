const { createInterface } = require("readline");


async function* read(file) {
  for await ( line of createInterface({ input: file }) ) {
    const parts = line.split(": ");
    const numbers = parts[1];
    yield splitNumbers(numbers);
  }
}

function splitNumbers(numbersPart) {
  const parts = numbersPart.split(" | ");
  const winnersTxt = parts[0].trim();
  const chosenTxt = parts[1].trim();

  return [winnersTxt.split(/\s+/), chosenTxt.split(/\s+/)];
}

function winnings(winners, chosen) {
  const chosenSet = new Set(chosen);
  const winnersSet = new Set(winners);
  let found = 0;
  for (const choice of chosenSet) {
    if (winnersSet.has(choice)) {
      found++;
    }
  }
  if ( found > 0 ) {
    return Math.pow(2, found - 1);
  }
  return 0;
}

async function main() {
  let total = 0;
  for await ( const [ winners, chosen ] of read(process.stdin) ) {
     const won = winnings(winners, chosen);
     total += won;
  }
  console.log(total);
}

if (require.main === module) {
  main();
}
