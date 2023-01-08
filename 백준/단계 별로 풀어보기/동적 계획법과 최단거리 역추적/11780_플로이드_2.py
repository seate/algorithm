import sys
input = sys.stdin.readline
IP = lambda: map(int, input().split())
INF = float("INF")

def solve():
    V = int(input())
    E = int(input())
    dist = [[INF] * V for i in range(V)]
    trace = [[[j + 1] for j in range(V)] for i in range(V)]
    
    for i in range(E):
        a, b, c = IP()
        if c < dist[a - 1][b - 1]: dist[a - 1][b - 1] = c
    
    for via in range(V):
        for start in range(V):
            if start == via: continue
            for dest in range(V):
                if via == dest or start == dest: continue
                if dist[start][via] + dist[via][dest] < dist[start][dest]:
                    dist[start][dest] = dist[start][via] + dist[via][dest]
                    trace[start][dest] = trace[start][via] + trace[via][dest]
    
    for i in range(V):
        for j in range(V):
            if dist[i][j] == INF: dist[i][j] = 0
    
    for i in dist: print(' '.join(map(str, i)))
    
    for i in range(V):
        for j in range(V):
            if not dist[i][j]: print('0'); continue
            print(f"{len(trace[i][j]) + 1} {i + 1}", ' '.join(map(str, trace[i][j])))
    
if "__main__" == __name__: solve()