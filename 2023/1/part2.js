

let total = 0;
const lookup = {
  '0': 0,
  '1': 1,
  'one': 1,
  '2': 2,
  'two': 2,
  '3': 3,
  'three': 3,
  '4': 4,
  'four': 4,
  '5': 5,
  'five': 5,
  '6': 6,
  'six': 6,
  '7': 7,
  'seven': 7,
  '8': 8,
  'eight': 8,
  '9': 9,
  'nine': 9,
}

const digits = /(?=(one|two|three|four|five|six|seven|eight|nine|\d))/g;
function processLine(line) {
  const match = Array.from(line.matchAll(digits)).map(m => m[1]);
  if (match.length > 0) {
    first = lookup[match[0]];
    last = lookup[match.pop()];

    total += 10 * first + last;
  }
}

process.stdin.resume();
process.stdin.setEncoding('utf8');


let lingeringLine = "";
process.stdin.on('data', function(chunk) {
    const lines = chunk.split("\n");

    lines[0] = lingeringLine + lines[0];
    lingeringLine = lines.pop();

    lines.forEach(processLine);
});

process.stdin.on('end', function() {
    processLine(lingeringLine);
    console.log(total);
});
