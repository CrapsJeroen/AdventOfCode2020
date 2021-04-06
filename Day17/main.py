def actives3D(grid, x, y, z):
    an = 0
    for dx in (-1, 0, 1):
        for dy in (-1, 0, 1):
            for dz in (-1, 0, 1):
                if dx == dy == dz == 0:
                    continue
                if grid.get((x + dx, y + dy, z + dz), False):
                    an += 1
    return an


def evolve3D(grid):
    new = {}
    for x in range(min(k[0] for k in grid.keys()) - 1, max(k[0] for k in grid.keys()) + 2):
        for y in range(min(k[1] for k in grid.keys()) - 1, max(k[1] for k in grid.keys()) + 2):
            for z in range(min(k[2] for k in grid.keys()) - 1, max(k[2] for k in grid.keys()) + 2):
                state = grid.get((x, y, z), False)
                an = actives3D(grid, x, y, z)

                if (state and an in (2, 3)) or (not state and an == 3):
                    new[(x, y, z)] = True
    return new


def actives4D(grid, x, y, z, q):
    an = 0
    for dx in (-1, 0, 1):
        for dy in (-1, 0, 1):
            for dz in (-1, 0, 1):
                for dq in (-1, 0, 1):
                    if dx == dy == dz == dq == 0:
                        continue
                    if grid.get((x + dx, y + dy, z + dz, q + dq), False):
                        an += 1
    return an


def evolve4D(grid):
    new = {}
    for x in range(min(k[0] for k in grid.keys()) - 1, max(k[0] for k in grid.keys()) + 2):
        for y in range(min(k[1] for k in grid.keys()) - 1, max(k[1] for k in grid.keys()) + 2):
            for z in range(min(k[2] for k in grid.keys()) - 1, max(k[2] for k in grid.keys()) + 2):
                for q in range(min(k[3] for k in grid.keys()) - 1, max(k[3] for k in grid.keys()) + 2):
                    state = grid.get((x, y, z, q), False)
                    an = actives4D(grid, x, y, z, q)

                    if (state and an in (2, 3)) or (not state and an == 3):
                        new[(x, y, z, q)] = True
    return new


with open("./input") as f:
    arr = [[i for i in l.rstrip()] for l in f]
    grid3D, grid4D = {}, {}

    for row, line in enumerate(arr):
        for col, ch in enumerate(line):
            grid3D[(row, col, 0)] = (ch == '#')
            grid4D[(row, col, 0, 0)] = (ch == '#')

    for i in range(6):
        print(i, sum(grid3D.values()))
        grid3D = evolve3D(grid3D)
    print(f"Problem 1: {sum(grid3D.values())}")

    for i in range(6):
        print(i, sum(grid4D.values()))
        grid4D = evolve4D(grid4D)
    print(f"Problem 2: {sum(grid4D.values())}")
