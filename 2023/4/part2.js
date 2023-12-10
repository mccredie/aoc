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
  return found;
}

async function main() {
  let total = 0;
  let i = 0;
  const multiplier = {};
  for await ( const [ winners, chosen ] of read(process.stdin) ) {
    const m = (multiplier[i] = multiplier[i] ?? 1);
    total += m;
    const won = winnings(winners, chosen);
    for (let j = i+1; j <= i + won; j++) {
      multiplier[j] = (multiplier[j] ?? 1) + m;
    }
    i++
  }
  console.log(total);
}

if (require.main === module) {
  main();
}
