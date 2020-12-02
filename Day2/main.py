import re


def process_one(a: str, b: str, char: str, string: str) -> bool:
    return (int(a) <= string.count(char) <= int(b))


def process_two(a: str, b: str, char: str, string: str) -> bool:
    return (string[int(a) - 1] == char) ^ (string[int(b) - 1] == char)


with open("./input") as f:
    arr = [re.split(r'\W+', i.rstrip()) for i in f]

    print(f"Valid passwords - Policy 1: {sum([process_one(*r) for r in arr])}")
    print(f"Valid passwords - Policy 2: {sum([process_two(*r) for r in arr])}")
