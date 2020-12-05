with open("./input") as f:
    m = {"B": '1', "R": '1', "F": '0', "L": '0'}
    bps = list(map(lambda x: int("".join(map(m.__getitem__, x)), 2), (l.rstrip() for l in f)))

    print(f"Problem 1: Highest Boardingpass ID = {max(bps)}")
    print(f"Problem 2: My Boardingpass ID = {next(iter(set(range(min(bps), max(bps))) - set(bps)))}")
