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

def main():
    rules, strings = read_input(sys.stdin)
    rule_table = parse_rules(rules)
    regex = rule_table['0'].to_regex(rule_table).join("^$")
    matcher = re.compile(regex)
    total = 0
    for string in strings:
        if m := matcher.match(string):
            total += 1
    print(total)

if __name__ == "__main__":
    main();
