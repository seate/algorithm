from collections import deque
from sys import stdin

def solve():
    buf = map(int, stdin.read().split())
    for T in range(next(buf)):
        V, E = next(buf), next(buf)
        edge = [[] for _ in range(V + 1)]
        visited = [0] * (V + 1)
        isit = True
        
        for _ in range(E):
            a, b = next(buf), next(buf)
            edge[a].append(b); edge[b].append(a)
        
        for i in range(1, V + 1):
            if visited[i]: continue #한번 bfs를 돌면 connected component 1개는 전부 완료되므로 not visited[i]라면 방문하지 않은 component라는 뜻
            visited[i] = 1
            que = deque([i])
            
            while que and isit:
                present = que.popleft()
                next_visited = visited[present] * -1
                for next_vertex in edge[present]:
                    if not visited[next_vertex]:
                        visited[next_vertex] = next_visited
                        que.append(next_vertex)
                    elif visited[next_vertex] == visited[present]: isit = False; break
            if not isit: break
        
        print("YES" if isit else "NO")
    
if "__main__" == __name__: solve()