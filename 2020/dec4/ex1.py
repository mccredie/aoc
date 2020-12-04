import sys

from helpers import Passports, Validator

def main():
    passports = Passports.from_lines(sys.stdin)
    validator = Validator("byr iyr eyr hgt hcl ecl pid".split())

    valid_passports = 0

    for passport in passports:
        valid_passports += validator.validate(passport)

    print(valid_passports)

if __name__ == "__main__":
    main()




