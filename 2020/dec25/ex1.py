
import sys
from itertools import count

def read_input(lines):
    card, door = list(lines)
    return int(card), int(door)

def transform_one(value, sub):
    return (value * sub) % 20201227

def transform(sub, loops):
    value = 1
    for _ in range(loops):
        value = transform_one(value, sub)
    return value

def find_loop(value, sub):
    v = 1
    for i in count(1):
        v = transform_one(v, sub)
        if v == value:
            break
    return i

def main():
    card, door = read_input(sys.stdin)
    card_loop = find_loop(card, 7)
    door_loop = find_loop(door, 7)
    print(transform(door, card_loop))
    print(transform(card, door_loop))



if __name__ == "__main__":
    main()
