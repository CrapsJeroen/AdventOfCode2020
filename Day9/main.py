from queue import Queue


def find_pair(target: int, arr: list) -> tuple:
    s = set()
    for num in arr:
        if (target - num) in s:
            return (num, target - num)
        else:
            s.add(num)
    return None


def find_range(target: int, arr: list) -> tuple:
    for idx, n in enumerate(arr):
        tmp = [n]
        for n2 in arr[idx + 1:]:
            tmp.append(n2)
            if target == sum(tmp):
                return min(tmp), max(tmp)
            elif target < sum(tmp):
                break


with open("./input") as f:
    arr = [int(l.rstrip()) for l in f]
    preamble_size = 25
    q = Queue(maxsize=preamble_size)

    for i in range(0, preamble_size):
        q.put(arr[i])

    for num in arr[preamble_size:]:
        if find_pair(num, list(q.queue)):
            q.get()
            q.put(num)
        else:
            print(f"Problem 1: {num}")
            break

    print(f"Problem 2: {sum(find_range(num, arr))}")
