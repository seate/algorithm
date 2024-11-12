import sys
sys.setrecursionlimit(10 ** 8)

def DFS(dic, key):
    for item in dic[key]:
        if visitable_for_dfs[item]:
            visitable_for_dfs[item] = False
            trace_for_dfs.append(item)
            DFS(dic, item)

def BFS(dic, key):
    result = [key] + dic[key]
    
    for i in result: visitable_for_bfs[i] = False
    
    for first in result:
        for second in dic[first]:
            if visitable_for_bfs[second]:
                result.append(second)
                visitable_for_bfs[second] = False
    
    return result
    


N, M, start = map(int, input().split())
save_dict = dict()
for i in range(1, N + 1): save_dict[i] = []
for i in range(M):
    a, b = map(int, input().split())
    save_dict[a] += [b]
    save_dict[b] += [a]
for key in save_dict: save_dict[key].sort()


trace_for_dfs = [start]
visitable_for_dfs = [True] * (N + 1)
visitable_for_dfs[start] = False
DFS(save_dict, start)
for i in trace_for_dfs: print(i, end = ' ')

print()

visitable_for_bfs = [True] * (N + 1)
visitable_for_bfs[start] = False
for i in BFS(save_dict, start): print(i, end = ' ')