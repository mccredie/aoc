
import sys


def get_expense_prod(lines, total):
    values = set()
    for value in lines:
        values.add(value)
        remainder = total - value
        if remainder in values:
            return remainder * value


def get_three_expense_prod(lines, total):
    values = set()
    for value in lines:
        values.add(value)
        remainder = total - value
        prod = get_expense_prod(lines, remainder)
        if prod is not None:
            return value * prod


def main():
    print(
        get_three_expense_prod(
            [int(line.strip()) for line in sys.stdin],
            2020
        )
    )


if __name__ == "__main__":
    main()
