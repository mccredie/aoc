import sys,re
from collections import defaultdict

re_rule = re.compile(r"^(?P<field>[^:]+): (?P<ranges>\d+-\d+( or (?P<range>\d+-\d+)))*$")
re_ranges = re.compile(r"^(\d+-\d+)(?: or (\d+-\d+))$")

def sections(lines):
    current_section = []
    for line in lines:
        line = line.strip()
        if line:
            current_section.append(line)
        else:
            yield current_section
            current_section = []
    yield current_section

def in_range_func(from_, to):
    def in_range(value):
        return from_ <= value <= to
    return in_range

def get_range(range_str):
    from_, to = range_str.split('-')
    return in_range_func(int(from_), int(to))

def get_ranges(ranges_str):
    for range_str in re_ranges.match(ranges_str).groups():
        yield get_range(range_str)

def combine_rules(rules):
    rules = list(rules)
    def match_rules(value):
        return any(rule(value) for rule in rules)
    return match_rules

def get_rule(rule_str):
    match = re_rule.match(rule_str)
    field =  match.group('field')
    ranges = list(get_ranges(match.group('ranges')))
    def match_rule(value):
        return any(in_range(value) for in_range in ranges)
    return field, match_rule

def get_rules(rules_sec):
    for rule_str in rules_sec:
        yield get_rule(rule_str)

def get_ticket(ticket_str):
    for value in ticket_str.split(","):
        yield int(value)

def get_valid_tickets(pred, tickets):
    for ticket in tickets:
        ticket = list(get_ticket(ticket))
        if all(pred(value) for value in ticket):
            yield ticket

def main():
    rules_sec, my_ticket_sec, other_tickets_sec = sections(sys.stdin)
    rules = dict(get_rules(rules_sec))
    violations = defaultdict(set)
    obeys_any = combine_rules(rules.values())
    tickets = get_valid_tickets(obeys_any, other_tickets_sec[1:])
    for ticket in tickets:
        for name, rule in rules.items():
            for i, value in enumerate(ticket):
                if not rule(value):
                    violations[name].add(i)

    my_ticket = list(get_ticket(my_ticket_sec[1]))
    all_indexes = set(range(len(my_ticket)))
    valid_indexes = {
            name: all_indexes - invalid
            for name, invalid in violations.items()
    }
    found = {}
    keep_going = True
    while keep_going:
        keep_going = False
        singles = []
        for name, indexes in valid_indexes.items():
            if len(indexes) == 1:
                found[name] = list(indexes)[0]
                singles.append(indexes)
            elif indexes:
                keep_going = True
        updates = {}
        for single in singles:
            for key, indexes in valid_indexes.items():
                updates[key] = indexes - single
        valid_indexes.update(updates)

    prod = 1
    for key, value in found.items():
        if key.startswith('departure'):
            prod *= my_ticket[value]
    print(prod)


if __name__ == "__main__":
    main()
