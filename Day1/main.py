def find_pair(target: int, arr: list) -> tuple:
    s = set()
    for num in arr:
        if (target - num) in s:
            return (num, target - num)
        else:
            s.add(num)
    return None, None


with open("./input") as f:
    arr = [int(i) for i in f]
    target = 2020

    a, b = find_pair(target, arr)
    print(f"{a} + {b} = {a+b} \nResult: {a * b}")

    for idx, a in enumerate(arr):
        b, c = find_pair(target - a, arr[idx:])
        if a and b:
            print(f"{a} + {b} + {c} = {a + b + c} \nResult: {a * b * c}")
            break
