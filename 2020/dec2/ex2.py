import sys


def main():
    valid_passwords = 0
    for line in sys.stdin:
        policy, password = line.split(':')
        checker = get_policy_checker(policy)
        valid_passwords += checker(password)
    print(valid_passwords)


def get_policy_checker(policy):
    counts, char = policy.split(' ')
    from_, to = (int(x) for x in counts.split('-'))

    def checker(password):
        return char_at(password, from_, char) + char_at(password, to, char) == 1

    return checker


def char_at(s, index, char):
    try:
        return s[index] == char
    except LookupError:
        return False


if __name__ == "__main__":
    main()
