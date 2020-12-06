from functools import reduce
from operator import and_, or_


with open("./input") as f:
    ls = [[set(c) for c in g.split('\n')] for g in f.read().split('\n\n')]

    print(f"Problem 1: {sum(map(len, (reduce(or_, l) for l in ls)))}")
    print(f"Problem 2: {sum(map(len, (reduce(and_, l) for l in ls)))}")
