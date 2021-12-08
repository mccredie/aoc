
import sys

def main():
    signals = read_signals(sys.stdin)
    total = 0
    for digits, inputs in signals:
        translation = build_translation(digits)
        total += get_value(translation, inputs)
    print(total)


def read_signals(lines):
    for line in lines:
        digits, inputs = (split_signals(part) for part in line.split("|"))
        yield digits, inputs

def get_value(translation, inputs):
    total = 0
    for digit in inputs:
        total *= 10
        total += translation[digit]
    return total

def build_translation(unknown):
    unknown = set(unknown)
    digits = {}
    for digit in unknown:
        length = len(digit)
        if length == 2:
            digits[1] = digit
        elif length == 4:
            digits[4] = digit
        elif length == 3:
            digits[7] = digit
        elif length == 7:
            digits[8] = digit

    unknown -= {digits[1], digits[4], digits[7], digits[8]}

    for digit in unknown:
        length = len(digit)
        if length == 6 and len(digit & digits[1]) == 1:
            digits[6] = digit
            break
    unknown.discard(digit)

    c = digits[8] - digits[6]
    f = digits[1] - c

    for digit in unknown:
        length = len(digit)
        if length == 5 and not c & digit:
            digits[5] = digit
            break
    unknown.discard(digit)

    for digit in unknown:
        length = len(digit)
        if length == 5 and not f & digit:
            digits[2] = digit
            break
    unknown.discard(digit)

    for digit in unknown:
        length = len(digit)
        if length == 5:
            digits[3] = digit
            break
    unknown.discard(digit)

    b = digits[8] - digits[2] - f
    d = digits[4] - digits[1] - b

    digits[0] = digits[8] - d

    unknown.discard(digits[0])

    digits[9] = unknown.pop()

    return {v:k for k,v in digits.items()}


def split_signals(line):
    return [frozenset(d) for d in line.strip().split()]

if __name__ == "__main__":
    main()
