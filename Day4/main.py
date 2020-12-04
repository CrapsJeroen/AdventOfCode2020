import re


def required_fields(passport: dict, fields: dict) -> bool:
    return all(fl in passport for fl in fields) or (sum(fl in passport for fl in fields) == 7 and 'cid' not in passport)


def check_height(v: str) -> bool:
    if v.endswith('cm'):
        return 150 <= int(v[:-2]) <= 193
    if v.endswith('in'):
        return 59 <= int(v[:-2]) <= 76
    return False


def validation(passport: dict, checks: dict) -> bool:
    if required_fields(passport, checks):
        return all(checks[k](v) for k, v in passport.items())
    return False


with open("./input") as f:
    ps, p = [], {}
    for l in f:
        if l.rstrip() == '':
            ps.append(p)
            p = {}
        else:
            fields = l.rstrip().split(" ")
            p.update({field[:3]: field[4:] for field in fields})
    ps.append(p)

    checks = {
        'byr': lambda v: 1920 <= int(v) <= 2002,
        'iyr': lambda v: 2010 <= int(v) <= 2020,
        'eyr': lambda v: 2020 <= int(v) <= 2030,
        'hgt': check_height,
        'hcl': lambda v: bool(re.match("^#(?:[0-9a-fA-F]{3}){1,2}$", v)),
        'pid': lambda v: bool(re.match("^[0-9]{9}$", v)),
        'ecl': lambda v: v in ('amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'),
        'cid': lambda v: True
    }

    print(f"""Problem 1: Valid passports = {sum(map(lambda x: required_fields(x, checks), ps))}""")
    print(f"""Problem 2: Valid passports = {sum(map(lambda x: validation(x, checks), ps))}""")
