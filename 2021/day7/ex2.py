import sys
from statistics import mean

def main():
    crab_positions = list(crab_positions_from_input(sys.stdin))

    last_value = per_crab_fuel(sum(crab_positions))

    for p in range(max(crab_positions)):
        fuel_spent = calc_fuel_spent(crab_positions, p)
        if fuel_spent > last_value:
            break
        last_value = fuel_spent

    print(last_value)

def calc_fuel_spent(crabs, center):
    return sum(per_crab_fuel(abs(c - center)) for c in crabs)

def per_crab_fuel(d):
    return int((d + 1) * (d / 2))

def crab_positions_from_input(lines):
    for line in lines:
        for crab_pos in line.split(","):
            yield int(crab_pos)

if __name__ == "__main__":
    main()
