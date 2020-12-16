
import sys,re

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

def main():
    rules_sec, my_tickt_sec, other_tickets_sec = sections(sys.stdin)
    rules = list(get_rules(rules_sec))
    obeys_any = combine_rules(rule for _, rule in rules)
    total = 0
    for ticket in other_tickets_sec[1:]:
        for value in get_ticket(ticket):
            if not obeys_any(value):
                total += value
    print(total)


if __name__ == "__main__":
    main()
