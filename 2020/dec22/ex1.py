import sys

def parse_players(lines):
    players = []
    player = []
    for line in lines:
        line = line.strip()
        if line.startswith('Player'):
            continue
        elif line:
            player.append(int(line))
        else:
            players.append(player)
            player = []
    players.append(player)
    return players

def play(p1, p2):
    while p1 and p2:
        c1 = p1.pop(0)
        c2 = p2.pop(0)
        if c1 > c2:
            winner = p1
        else:
            winner = p2
        winner.append(max(c1, c2))
        winner.append(min(c1, c2))

    return p1 or p2

def score(cards):
    return sum(i * c for i, c in enumerate(reversed(cards), 1))

def main():
    winner = play(*parse_players(sys.stdin))
    print(score(winner))


if __name__ == "__main__":
    main()
