import sys

def main():
    total = 0
    for l, w, h in packages(sys.stdin):
        total += total_area(l, w, h)
    print(total)

def packages(inputs):
    for line in inputs:
        yield tuple(int(x) for x in line.split("x"))

def total_area(l, w, h):
    areas = [l*w, l*h, w*h]
    smallest_face = min(areas)
    return sum(areas) * 2 + smallest_face

if __name__ == "__main__":
    main()

