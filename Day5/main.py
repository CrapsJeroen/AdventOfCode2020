with open("./input") as f:
    m = str.maketrans('FBLR', '0101')
    bps = list(map(lambda x: int(x.translate(m), 2), (l.rstrip() for l in f)))

    print(f"Problem 1: Highest Boardingpass ID = {max(bps)}")
    print(f"Problem 2: My Boardingpass ID = {next(iter(set(range(min(bps), max(bps))) - set(bps)))}")
