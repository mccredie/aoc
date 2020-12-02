
import sys


def get_expense_prod(lines, total):
    values = set()
    for value in lines:
        values.add(value)
        remainder = total - value
        if remainder in values:
            break
    return remainder * value


def main():
    print(
        get_expense_prod(
            [int(line.strip()) for line in sys.stdin],
            2020
        )
    )


if __name__ == "__main__":
    main()
