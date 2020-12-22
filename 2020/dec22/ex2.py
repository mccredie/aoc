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
    rounds = set()
    while p1 and p2:
        round = tuple(p1), tuple(p2)
        if round in rounds:
            return True, p1
        rounds.add(round)
        c1 = p1.pop(0)
        c2 = p2.pop(0)
        if len(p1) >= c1 and len(p2) >= c2:
             p1wins, cards = play(p1[:c1], p2[:c2])
             if p1wins:
                 p1 += [c1, c2]
             else:
                 p2 += [c2, c1]
        elif c1 > c2:
            p1 += [c1, c2]
        else:
            p2 += [c2, c1]

    return bool(p1), p1 or p2

def score(cards):
    return sum(i * c for i, c in enumerate(reversed(cards), 1))

def main():
    p1wins, cards = play(*parse_players(sys.stdin))
    print(score(cards))


if __name__ == "__main__":
    main()
