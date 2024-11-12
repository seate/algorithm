import sys
from math import log2
from collections import deque
input = sys.stdin.readline
IP = lambda: map(int, input().split())

INF = float("inf")

def solve():
    N = int(input())
    logN = int(log2(N)) + 1
    edge = [dict() for _ in range(N + 1)]
    depth = [0] * (N + 1)
    ancestor = [[-1] * logN for i in range(N + 1)]; ancestor[1][0] = 0
    big = [[0] * logN for i in range(N + 1)]
    small = [[INF] * logN for i in range(N + 1)]
    
    for _ in range(N - 1):
        a, b, cost = IP()
        edge[a][b] = cost; edge[b][a] = cost
    
    q = deque([1])
    while q:
        present = q.popleft()
        for i in edge[present]:
            if ancestor[i][0] == -1:
                q.append(i)
                ancestor[i][0] = present
                big[i][0] = small[i][0] = edge[present][i]
                depth[i] = depth[present] + 1
    
    for j in range(1, logN):
        for i in range(1, N + 1):
            ancestor[i][j] = ancestor[ancestor[i][j - 1]][j - 1]
            big[i][j] = big[i][j - 1] if big[ancestor[i][j - 1]][j - 1] < big[i][j - 1] else big[ancestor[i][j - 1]][j - 1]
            small[i][j] = small[i][j - 1] if small[i][j - 1] < small[ancestor[i][j - 1]][j - 1] else small[ancestor[i][j - 1]][j - 1]
    
    
    for _ in range(int(input())):
        a, b = IP()
        present_big = 0; present_small = INF
        if depth[b] < depth[a]: a, b = b, a
        differ = depth[b] - depth[a]
        
        for i in range(logN):
            if differ & (1 << i):
                if present_big < big[b][i]: present_big = big[b][i]
                if small[b][i] < present_small: present_small = small[b][i]
                b = ancestor[b][i]
        
        if a != b:
            for i in range(logN - 1, -1, -1):
                if ancestor[a][i] != ancestor[b][i]:
                    if present_big < big[a][i]: present_big = big[a][i]
                    if small[a][i] < present_small: present_small = small[a][i]
                    if present_big < big[b][i]: present_big = big[b][i]
                    if small[b][i] < present_small: present_small = small[b][i]
                    a = ancestor[a][i]; b = ancestor[b][i]
            
            if present_big < big[a][i]: present_big = big[a][i]
            if small[a][i] < present_small: present_small = small[a][i]
            if present_big < big[b][i]: present_big = big[b][i]
            if small[b][i] < present_small: present_small = small[b][i]
        
        print(present_small, present_big)
    
if "__main__" == __name__: solve()