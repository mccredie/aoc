import sys
from collections import defaultdict

def read_input():
    return [int(line.strip()) for line in sys.stdin]

def find_oddball(seq, prefix):
    not_found = set()
    searching = defaultdict(set)
    for i, x in enumerate(seq[:len(seq) - prefix]):
        vi = i + prefix
        v = seq[vi]
        searching[v].add(vi)
        not_found.add(prefix + i)
        for y in seq[i + 1: i + prefix]:
            if x != y:
                not_found.difference_update(searching[x + y])
        if i in not_found:
            return seq[i]

def find_weakness(seq, target):
    start = 0
    stop = 2
    total = sum(seq[start: stop])
    while True:
        if total < target:
            total += seq[stop]
            stop += 1
        elif total > target:
            total -= seq[start]
            start += 1
        else:
            return max(seq[start: stop]) + min(seq[start: stop])

def main():
    seq = read_input()
    oddball = find_oddball(seq, 25)
    print(oddball)
    print(find_weakness(seq, oddball))


if __name__ == "__main__":
    main()
