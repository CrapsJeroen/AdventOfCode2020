from collections import Counter
from functools import reduce

all_foods = set()
times = Counter()

pos = {}

with open('./input') as f:
    arr = [l.strip() for l in f]
    for line in arr:
        a, b = line.split(" (contains ")
        foods = set(a.split())
        algs = set(b[:-1].split(", "))

        all_foods |= foods
        times.update(foods)

        for alg in algs:
            if alg not in pos:
                pos[alg] = foods.copy()
            else:
                pos[alg] &= foods

bad = set(reduce(lambda a, b: a | b, pos.values()))

print(f"Problem 1: {sum(times[food] for food in (all_foods - bad))}")

taken = set()
items = []
while True:
    for alg, foods in pos.items():
        if len(foods - taken) == 1:
            rem = min(foods - taken)
            items.append((alg, rem))
            taken.add(rem)
            break
    else:
        break

print(",".join(x[1] for x in sorted(items)))
