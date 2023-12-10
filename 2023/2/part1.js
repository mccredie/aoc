const { createInterface } = require('readline');

async function main() {
  let total = 0;
  const games = await readGames();
  for ( const game of games ) { 
    if (isGamePossible(game)) {
      total += game.id;
    }
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

const maximums = {
  red: 12,
  green: 13,
  blue: 14,
}

function isGrabPossible(grab) { 
  return Object.entries(grab).every(([color, count]) => {
    const color_max = maximums[color] ?? 0;
    return count <= color_max;
  })
}

function isGamePossible(game) {
  return game.grabs.every(isGrabPossible);
}


if (require.main === module) {
  main()
}


