from copy import deepcopy


with open("./input") as f:
    arr = [tuple(l.split()) for l in f]

    ACC = i = 0
    v = set()
    while i not in v:
        v.add(i)
        op, val = arr[i]
        i += int(val) if op == 'jmp' else 1
        ACC += int(val) if op == 'acc' else 0

    print(f"Problem 1: {ACC}")

    ACC = i = j = 0
    v = set()
    while j < len(arr):
        v.add(i)
        op, val = arr[i]
        if op in ('jmp', 'nop'):
            w = deepcopy(v)
            ACC2 = ACC
            j = i + (int(val) if op == 'nop' else 1)
            while j not in w and j < len(arr):
                w.add(j)
                op2, val2 = arr[j]
                j += int(val2) if op2 == 'jmp' else 1
                ACC2 += int(val2) if op2 == 'acc' else 0

        i += int(val) if op == 'jmp' else 1
        ACC += int(val) if op == 'acc' else 0
    print(f"Problem 2: {ACC2}")
