from collections import deque
import sys
input = sys.stdin.readline
IP = lambda: map(int, input().split())

def bfs_solve():
    T = 1
    while True:
        V, E = IP()
        if not (V or E): break
        count = 0; parent = [0] * (V + 1)
        edge = [[] for i in range(V + 1)]
        for i in range(E):
            a, b = IP()
            edge[a].append(b); edge[b].append(a)
        
        for start in range(1, V + 1):
            if not parent[start]:
                parent[start] = -1
                istree = True
                q = deque([start])
                while q:
                    present = q.popleft()
                    for next_vertex in edge[present]:
                        if parent[present] != next_vertex:
                            if not parent[next_vertex]:
                                parent[next_vertex] = present
                                q.append(next_vertex)
                            else: istree = False
                count += istree
        
        if not count: print(f"Case {T}: No trees.")
        elif count == 1: print(f"Case {T}: There is one tree.")
        else: print(f"Case {T}: A forest of {count} trees.")
        T += 1

def dfs_solve(): #faster
    def dfs(node, prev):
        visited[node] = True
        is_cycle = False
        for nv in edge[node]:
            if nv != prev:
                if visited[nv]: return True
                else: is_cycle = is_cycle or dfs(nv, node)
        return is_cycle
    
    T = 1
    while True:
        V, E = IP()
        if not (V or E): break
        count = 0; visited = [False] * (V + 1)
        edge = [[] for i in range(V + 1)]
        for i in range(E):
            a, b = IP()
            edge[a].append(b); edge[b].append(a)
        
        for node in range(1, V + 1):
            if not visited[node] and not dfs(node, 0): count += 1
        
        if not count: print(f"Case {T}: No trees.")
        elif count == 1: print(f"Case {T}: There is one tree.")
        else: print(f"Case {T}: A forest of {count} trees.")
        T += 1
    
if "__main__" == __name__:
    #bfs_solve()
    dfs_solve()