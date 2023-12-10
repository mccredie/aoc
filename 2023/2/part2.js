const { createInterface } = require('readline');

async function main() {
  let total = 0;
  const games = await readGames();
  for ( const game of games ) { 
    const power = gamePower(game);
    total += power;
  }
  console.log(total);
}

async function readGames() {
  const games = [];
  for await (const line of createInterface({ input: process.stdin })) {
    const match = line.match(/^Game (?<game>\d+): (?<rest>.*)$/);
    if (match) {
      const grabs = match.groups.rest.split('; ');
      const game = Number.parseInt(match.groups.game);
      const game_obj = { id: game, grabs: [] };
      for (const grab_txt of grabs) {
        const colors = grab_txt.split(', ');
        const grab = {};
        for (const color_group of colors) {
          const [count_txt, color] = color_group.split(' ');
          const count = Number.parseInt(count_txt);
          grab[color] = count;
        }
        game_obj.grabs.push(grab);
      }
      games.push(game_obj);
    }
  }
  return games;
}

function getMinimum(grab, minimums) { 
  Object.entries(grab).forEach(([color, count]) => {
    const current_min = minimums[color];
    minimums[color] = Math.max(current_min, count);
  })
}

function gamePower(game) {
  const minimums = {
    red: 0,
    green: 0,
    blue: 0,
  }
  game.grabs.forEach((grab) => {
    getMinimum(grab, minimums)
  })
  return minimums.red * minimums.green * minimums.blue;
}

if (require.main === module) {
  main()
}
