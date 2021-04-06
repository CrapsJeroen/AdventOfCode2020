from collections import defaultdict
from operator import mul
from functools import reduce

with open("./input") as f:
    contents = [l.split('\n') for l in f.read().split('\n\n')]
    d = {int(c[0][5:-1]): [[l for l in w.rstrip()] for w in c[1:]] for c in contents}

    edge_dict = defaultdict(list)

    for k, v in d.items():
        edge_dict["".join(v[0])].append(k)
        edge_dict["".join(v[0])[::-1]].append(k)
        edge_dict["".join(v[-1])].append(k)
        edge_dict["".join(v[-1][::-1])].append(k)
        edge_dict["".join([i[0] for i in v])].append(k)
        edge_dict["".join([i[0] for i in v][::-1])].append(k)
        edge_dict["".join([i[-1] for i in v])].append(k)
        edge_dict["".join([i[-1] for i in v][::-1])].append(k)

    tile_edges = defaultdict(lambda: 0)
    for k, v in edge_dict.items():
        if len(v) > 1:
            for idx in v:
                tile_edges[idx] += 1

    print(tile_edges)
    print(reduce(mul, [k for k, v in tile_edges.items() if v == 4]))

    # rules = list(filter(lambda l: ':' in l, arr))
    # strings = list(filter(lambda l: ':' not in l, arr))

    # rules = dict(rule.split(': ', 1) for rule in rules)

    # regex = generate_regex('0', False)
    # print(f"Problem 1: {sum(1 if re.fullmatch(regex, l) else 0 for l in strings)}")

    # regex = generate_regex('0', True)
    # print(f"Problem 2: {sum(1 if re.fullmatch(regex, l) else 0 for l in strings)}")
