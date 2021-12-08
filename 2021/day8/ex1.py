
import sys

def main():
    signals = read_signals(sys.stdin)
    known = 0
    for _, inputs in signals:
        for segment in inputs:
            known += is_known(segment)
    print(known)

def read_signals(lines):
    for line in lines:
        pattern, inputs = (split_signals(part) for part in line.split("|"))
        yield pattern, inputs

def is_known(segment):
    length = len(segment)
    return length in (2, 4, 3, 7)


def split_signals(line):
    return line.strip().split()

if __name__ == "__main__":
    main()
