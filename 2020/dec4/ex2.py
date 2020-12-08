
import sys, re

from helpers import Passports, Validator


class PassportValidator(Validator):
    def __init__(self):
        super().__init__("byr iyr eyr hgt hcl ecl pid".split())

    def validate_byr(self, value):
        return 1920 <= int(value) <= 2002

    def validate_iyr(self, value):
        return 2010 <= int(value) <= 2020

    def validate_eyr(self, value):
        return 2020 <= int(value) <= 2030

    hgt = re.compile("^(?P<height>\d+)(?P<units>in|cm)$")
    def validate_hgt(self, value):
        if match := self.hgt.match(value):
            height = int(match.group("height"))
            units = match.group("units")
            return (
                    (units == "cm" and 150 <= height <= 193)
                    or (units == "in" and 59 <= height <= 76)
            )
        return False

    hcl = re.compile(r"^#[a-f0-9]{6}$")
    def validate_hcl(self, value):
        return self.hcl.match(value) is not None

    def validate_ecl(self, value):
        return value in ("amb", "blu", "brn", "gry", "grn", "hzl", "oth")

    pid = re.compile(r'^\d{9}$')
    def validate_pid(self, value):
        return self.pid.match(value) is not None


def main():
    passports = Passports.from_lines(sys.stdin)
    validator = PassportValidator()

    valid_passports = 0

    for passport in passports:
        valid_passports += validator.validate(passport)

    print(valid_passports)

if __name__ == "__main__":
    main()
