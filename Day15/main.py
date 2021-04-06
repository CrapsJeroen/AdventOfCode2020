with open("./input") as f:
    d = {int(i.rstrip()): idx + 1 for l in f for idx, i in enumerate(l.split(','))}
    last = list(d)[-1]

    for i in range(len(d), 30000000):
        d[last], last = i, i - d[last] if last in d else 0
        if i == 2020 - 1:
            print(f"Problem 1: {last}")
        if i == 30000000 - 1:
            print(f"Problem 2: {last}")
