import sys

def main():
    co2 = o2 = [split_line(line) for line in sys.stdin]
    bits = len(co2[0])


    for i in range(bits):
        co2_count = len(co2)
        if co2_count == 1:
            break;
        co2_bit_value = sum(gen_pos(co2, i)) >= co2_count / 2
        co2 = list(filter(lambda line: line[i] == co2_bit_value, co2))

    for i in range(bits):
        o2_count = len(o2)
        if o2_count == 1:
            break;
        o2_bit_value = sum(gen_pos(o2, i)) >= o2_count / 2
        o2 = list(filter(lambda line: line[i] != o2_bit_value, o2))

    print(bin_to_dec(co2[0]) * bin_to_dec(o2[0]))

def bin_to_dec(bval):
    value = 0
    for b in bval:
        value *= 2
        value += b
    return value

def gen_pos(rows, pos):
    return (r[pos] for r in rows)

def split_line(value):
    return tuple(int(x) for x in value.strip())


if __name__ == "__main__":
    main()
