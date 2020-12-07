import re


with open("./input") as f:
    tree = {
        parent: [
            (
                0 if x[0] == 'no' else int(x[0]),
                ' '.join(x[1:])
            ) for x in (x.split() for x in children)
        ] for parent, *children in map(lambda x: re.findall(r'(\d?\s?\w+\s\w+) bag', x), f.readlines())
    }

    def in_bag(parent, bag):
        return any(1 for _, child in tree.get(parent, [(0, None)]) if child == bag or child and in_bag(child, bag))

    def count_bags(bag):
        return 1 + sum(v * count_bags(c) if c else 0 for v, c in tree.get(bag, [(0, None)]))

    print(f"Problem 1: {sum(in_bag(x, 'shiny gold') for x in tree.keys())}")
    print(f"Problem 2: {count_bags('shiny gold')-1}")
