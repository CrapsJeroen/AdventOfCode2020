from operator import add
from copy import deepcopy


nav = {0: 'E', 90: 'S', 180: 'W', 270: 'N'}

with open("./input") as f:
    arr = [(l[0], int(l.rstrip()[1:])) for l in f]

    facing = 0
    mov = deepcopy(arr)
    for k, v in filter(lambda x: x[0] in 'FRL', arr):
        if k == 'F':
            mov.append((nav[facing], v))
        else:
            facing = (facing + (-v if k == 'L' else v)) % 360

    y = sum(-x[1] if x[0] == 'S' else x[1] for x in filter(lambda x: x[0] in 'NS', mov))
    x = sum(-x[1] if x[0] == 'W' else x[1] for x in filter(lambda x: x[0] in 'EW', mov))

    print(f"Problem 1: {sum(map(lambda a: abs(a[0]-a[1]), zip((0, 0), (x, y))))}")

    nav = (10, 1)
    ship = (0, 0)

    for k, v in [(k, -v if k in 'SW' else v) for k, v in arr]:
        if k in 'NESW':
            nav = tuple(map(add, nav, ((0, v) if k in 'NS' else (v, 0))))
        elif k in 'L':
            for i in range(v // 90):
                nav = (-nav[1], nav[0])
        elif k in 'R':
            for i in range(v // 90):
                nav = (nav[1], -nav[0])
        elif k == 'F':
            ship = tuple(map(add, ship, (v * nav[0], v * nav[1])))

    print(f"Problem 2: {sum(map(lambda a: abs(a[0]-a[1]), zip((0, 0), ship)))}")
