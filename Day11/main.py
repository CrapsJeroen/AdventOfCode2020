from copy import deepcopy
from itertools import product


def occupied_seats(arr, idx, jdx):
    l1 = [idx + i for i in [-1, 0, +1] if 0 <= idx + i < len(arr)]
    l2 = [jdx + j for j in [-1, 0, +1] if 0 <= jdx + j < len(arr[idx])]
    all_c = [t for t in product(l1, l2) if t != (idx, jdx)]

    return sum(arr[i][j] == '#' for (i, j) in all_c)


def occupied_seats2(arr, idx, jdx):
    occ = 0

    for i, j in [t for t in product([-1, 0, +1], [-1, 0, +1]) if t != (0, 0)]:
        x, y = idx, jdx
        while True:
            x, y = x + i, y + j
            if not (0 <= x < len(arr) and 0 <= y < len(arr[idx])):
                break
            if arr[x][y] != '.':
                occ += int(arr[x][y] == '#')
                break

    return occ


def evolve(arr):
    tmp = deepcopy(arr)
    for idx, row in enumerate(arr):
        for jdx, val in enumerate(row):
            if val == 'L' and occupied_seats(arr, idx, jdx) == 0:
                tmp[idx][jdx] = '#'
            elif val == '#' and occupied_seats(arr, idx, jdx) >= 4:
                tmp[idx][jdx] = 'L'
    return tmp


def evolve2(arr):
    tmp = deepcopy(arr)
    for idx, row in enumerate(arr):
        for jdx, val in enumerate(row):
            if val == 'L' and occupied_seats2(arr, idx, jdx) == 0:
                tmp[idx][jdx] = '#'
            elif val == '#' and occupied_seats2(arr, idx, jdx) >= 5:
                tmp[idx][jdx] = 'L'
    return tmp


with open("./input") as f:
    arr = [[i for i in l.rstrip()] for l in f]

    a = deepcopy(arr)
    while True:
        new_arr = evolve(a)
        if new_arr == a:
            break
        a = new_arr

    print(f"Problem 1: {sum(l.count('#') for l in new_arr)}")

    a = deepcopy(arr)
    while True:
        new_arr2 = evolve2(a)
        if new_arr2 == a:
            break
        a = new_arr2

    print(f"Problem 2: {sum(l.count('#') for l in new_arr2)}")
