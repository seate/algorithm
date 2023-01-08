def DFS(dic, key):
    for item in dic[key]:
        if visitable_for_dfs[item]:
            visitable_for_dfs[item] = False
            DFS(dic, item)

N, M = int(input()), int(input())
start = 1

connected = dict()
for i in range(M):
    a, b = map(int, input().split())
    if a in connected: connected[a] += [b]
    else: connected[a] = [b]
    
    if b in connected: connected[b] += [a]
    else: connected[b] = [a]

visitable_for_dfs = [True] * (N + 1)
visitable_for_dfs[start] = False
DFS(connected, start)
print(visitable_for_dfs[2:].count(False))