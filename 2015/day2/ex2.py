import sys

def main():
    total = 0
    for l, w, h in packages(sys.stdin):
        total += total_circ(l, w, h)
    print(total)

def packages(inputs):
    for line in inputs:
        yield tuple(int(x) for x in line.split("x"))

def total_circ(l, w, h):
    circs = [l+w, l+h, w+h]
    smallest_circ = min(circs)
    return 2 * smallest_circ + l * h * w

if __name__ == "__main__":
    main()

