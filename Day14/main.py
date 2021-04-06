import re


def process(line, mask):
    return int("".join([y if y != 'X' else x for x, y in zip(bin(int(line))[2:].zfill(len(mask)), mask)]), 2)


def allmasks(mask):
    if not mask:
        yield ''
        return
    for m in allmasks(mask[1:]):
        if mask[0] == '0':
            yield 'X' + m
        elif mask[0] == '1':
            yield '1' + m
        elif mask[0] == 'X':
            yield '0' + m
            yield '1' + m


with open("./input") as f:
    d1, d2 = {}, {}
    for l in f:
        line = l.rstrip()
        if 'mask' in line:
            mask = line.split("=")[1].lstrip()
        else:
            pos = int(re.findall(r"mem\[(\d+)\].*", line)[0])
            process(pos, mask)
            d1[pos] = process(line.split('=')[1].lstrip(), mask)

            for m in allmasks(mask):
                d2[process(pos, m)] = int(line.split('=')[1].lstrip())

    print(f"Problem 1: {sum(d1.values())}")
    print(f"Problem 2: {sum(d2.values())}")
