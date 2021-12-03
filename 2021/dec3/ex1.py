import sys

def main():
    lines = [split_line(line) for line in sys.stdin]
    sums = [sum(col) for col in zip(*lines)]

    line_count = len(lines)

    gamma = bin_to_dec(s > line_count / 2 for s in sums)
    epsilon = bin_to_dec(s < line_count / 2 for s in sums)

    print(gamma * epsilon)


def bin_to_dec(bval):
    value = 0
    for b in bval:
        value *= 2
        value += b
    return value

def split_line(value):
    return tuple(int(x) for x in value.strip())


if __name__ == "__main__":
    main()
