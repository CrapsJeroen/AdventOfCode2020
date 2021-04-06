import re


def generate_regex(idx, part2=False):
    if part2:
        if idx == '8':
            return generate_regex('42', part2) + '+'
        elif idx == '11':
            a = generate_regex('42', part2)
            b = generate_regex('31', part2)
            return '(?:' + '|'.join(f'{a}{{{n}}}{b}{{{n}}}' for n in range(1, 10)) + ')'

    rule = rules[idx]
    if re.fullmatch(r'"[a-z]+"', rule):
        return rule[1]

    return '(?:' + '|'.join([''.join([generate_regex(num, part2) for num in part.split()]) for part in rule.split(' | ')]) + ')'


with open("./input") as f:
    arr = [l.rstrip() for l in f]
    rules = list(filter(lambda l: ':' in l, arr))
    strings = list(filter(lambda l: ':' not in l, arr))

    rules = dict(rule.split(': ', 1) for rule in rules)

    regex = generate_regex('0', False)
    print(f"Problem 1: {sum(1 if re.fullmatch(regex, l) else 0 for l in strings)}")

    regex = generate_regex('0', True)
    print(f"Problem 2: {sum(1 if re.fullmatch(regex, l) else 0 for l in strings)}")
