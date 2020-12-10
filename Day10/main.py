from collections import Counter
from itertools import groupby
from functools import reduce
from operator import mul


with open("./input") as f:
    arr = [int(l.rstrip()) for l in f]
    arr = [0] + sorted(arr) + [max(arr) + 3]

    diffs = list(map(lambda x, y: y - x, arr[:-1], arr[1:]))

    c = Counter(diffs)
    print(f"Problem 1: {c[3] * c[1]}")

    c2 = Counter([i for i in [sum(1 for _ in group) for val, group in groupby(diffs) if val == 1] if i != 1])
    pattern = [1, 1, 2, 4, 7]
    print(f"Problem 2: {reduce(mul, (pattern[k] ** v for k, v in c2.items()))}")
