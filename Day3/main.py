from functools import reduce
from operator import mul


def trees_in_path(area: list, mov: tuple) -> int:
    trees = x = y = 0
    height, width = len(area), len(area[0])
    while y < height:
        trees += area[y][x]
        x, y = ((x + mov[0]) % width), (y + mov[1])
    return trees


with open("./input") as f:
    area = [[i == '#' for i in line.rstrip()] for line in f]
    maneuvers = [(3, 1), (1, 1), (5, 1), (7, 1), (1, 2)]

    print(f"Problem 1: Amount of Trees = {trees_in_path(area, maneuvers[0])}")
    print(f"Problem 2: Multiplication of Trees = {reduce(mul, (trees_in_path(area, x) for x in maneuvers))}")
