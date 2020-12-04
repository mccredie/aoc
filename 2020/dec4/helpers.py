class Passports:
    def __init__(self):
        self.passports = []
        self.current_passport = {}

    def add_field(self, key, value):
        self.current_passport[key] = value

    def store(self):
        if self.current_passport:
            self.passports.append(self.current_passport)
            self.current_passport = {}

    def __iter__(self):
        return iter(self.passports)

    @staticmethod
    def from_lines(lines):
        """Lines can be a file."""
        passports = Passports()
        for line in lines:
            entries = line.split()
            if not entries:
                passports.store()
            else:
                for entry in entries:
                    key, value = entry.split(":")
                    passports.add_field(key, value)
        passports.store()
        return passports


class Validator:
    def __init__(self, required_fields):
        self.required_fields = required_fields

    def validate(self, d):
        return (
            all(
                field in d
                for field in self.required_fields
            )
            and all(
                self._validate_field(field, value)
                for field, value in d.items()
            )
        )

    def _validate_field(self, key, value):
        validate = getattr(self, f'validate_{key}', _ignore)
        return validate(value)


def _ignore(value):
    return True
