#!/usr/bin/env python3

import sys, re

class OR:
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def to_regex(self, lookup):
        left = self.left.to_regex(lookup)
        right = self.right.to_regex(lookup)
        return f"({left}|{right})"

class AND:
    def __init__(self, expressions):
        self.expressions = tuple(expressions)

    def to_regex(self, lookup):
        return "".join(lookup[e].to_regex(lookup) for e in self.expressions)

class LITERAL:
    def __init__(self, value):
        self.value = value

    def to_regex(self, lookup):
        return self.value

def read_input(lines):
    rules = []
    for line in lines:
        line = line.strip()
        if line:
            rules.append(line)
        else:
            break

    strings = []
    for line in lines:
        strings.append(line.strip())

    return rules, strings

def parse_rule_entry(entry_str):
    key, value = entry_str.split(':')
    return key, parse_rule(value)

def parse_rule(value):
    value = value.strip()
    if '"' in value:
        return LITERAL(value.strip('"'))
    elif '|' in value:
        left, right = (parse_rule(v) for v in value.split('|'))
        return OR(left, right)
    else:
        return AND(value.split(' '))

def parse_rules(lines):
    return dict(parse_rule_entry(rule) for rule in lines)

def recursive_match(regex, group, string):
    while string:
        print(string)
        if match := regex.match(string):
            string = match.group(group)
        else:
            print('not matched')
            return False
    print('matched')
    return True

def wrap_match(leftre, rightre, string):
    print("left:", leftre)
    print("right:", rightre)
    print("string:", string)
    regex = "(?P<middle>.*)"
    while True:
        matcher = re.compile(regex.join("^$"))
        if match := matcher.match(string):
            print("matched", match.group("middle"))
            if match.group('middle'):
                regex = f"{leftre}{regex}{rightre}"
            else:
                return True
        else:
            return False

def main():
    rules, strings = read_input(sys.stdin)
    rule_table = parse_rules(rules)

    regex42 = rule_table['42'].to_regex(rule_table)
    regex31 = rule_table['31'].to_regex(rule_table)

    # 0: 8 11
    # 8:42 | 42 8
    # 11:42 31 | 42 11 31

    regex = f"^(?P<_42s>{regex42}+)(?P<_31s>{regex31}+)$"
    matcher = re.compile(regex)
    match42 = re.compile(regex42)
    match31 = re.compile(regex31)

    total = 0
    for string in strings:
        if m := matcher.match(string):
            _42s = m.group("_42s")
            n_42s = len(match42.findall(_42s))
            _31s = m.group("_31s")
            n_31s = len(match31.findall(_31s))
            total += n_42s > n_31s

    print(total)


if __name__ == "__main__":
    main();
