def solve():
    N = int(input())
    mapping = dict()
    idxset = set(i for i in range(1, N + 1))
    s2 = set()

    for i in range(1, N + 1):
        cur = int(input())
        mapping[i] = cur
        s2.add(cur)

    while True:
        안겹 = idxset - s2
        if not 안겹: break

        idxset -= 안겹
        s2 = set(mapping[i] for i in idxset)

    print(len(idxset))
    for r in idxset: print(r)

solve()