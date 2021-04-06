from collections import deque
from copy import deepcopy


def game(p1d, p2d, seen):
    while p1d and p2d:
        zs = tuple(p1d)
        if zs in seen:
            return True
        seen.add(zs)

        p1, p2 = p1d.pop(0), p2d.pop(0)

        if p1 <= len(p1d) and p2 <= len(p2d):
            winner = game(p1d[:p1], p2d[:p2], set())
        else:
            winner = p2 < p1

        if winner:
            p1d.extend((p1, p2))
        else:
            p2d.extend((p2, p1))

    return bool(p1d)


with open('./input') as f:
    p1d, p2d = deque([]), deque([])
    p2dstart = False

    for i in [l.rstrip() for l in f][1:]:
        if i.isdigit() and not p2dstart:
            p1d.append(int(i))
        elif i.isdigit() and p2dstart:
            p2d.append(int(i))
        else:
            p2dstart = True

    cleanp1d, cleanp2d = deepcopy(p1d), deepcopy(p2d)

    while p1d and p2d:
        p1, p2 = p1d.popleft(), p2d.popleft()
        if p2 < p1:
            p1d.extend((p1, p2))
        else:
            p2d.extend((p2, p1))

    ans = 0
    for i, x in enumerate(reversed(p1d or p2d), 1):
        ans += i * x
    print(ans)

    p1d, p2d = list(cleanp1d), list(cleanp2d)
    game(p1d, p2d, set())

    ans = 0
    for i, x in enumerate(reversed(p1d or p2d), 1):
        ans += (i * x)
    print(ans)
