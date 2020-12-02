import sys


def get_policy_checker(policy):
    counts, char = policy.split(' ')
    from_, to = (int(x) for x in counts.split('-'))

    def checker(password):
        found = 0
        for c in password:
            if c == char:
                found += 1
            if found > to:
                return False
        return found >= from_
    return checker


def main():
    valid_passwords = 0
    for line in sys.stdin:
        policy, password = line.split(':')
        checker = get_policy_checker(policy)
        valid_passwords += checker(password)
    print(valid_passwords)

if __name__ == "__main__":
    main()
