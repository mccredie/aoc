
let total = 0;

function processLine(line) {
  let first = undefined;
  let last = undefined;
  for( c of line ) {
    const value = Number.parseInt(c);
    if (!isNaN(value)) {
      first = first === undefined ? value : first;
      last = value;
    }
  }

  if (typeof first === "number" && typeof last === "number") {
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
