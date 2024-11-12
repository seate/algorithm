import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 8)

def DFS(y, x):
    visitable[y][x] = False
    if y != 0 and visitable[y - 1][x]: DFS(y - 1, x)
    if y != N - 1 and visitable[y + 1][x]: DFS(y + 1, x)
    if x != 0 and visitable[y][x - 1]: DFS(y, x - 1)
    if x != M - 1 and visitable[y][x + 1]: DFS(y, x + 1)


for T in range(int(input())):
    M, N, K = map(int, input().split())
    visitable = [[False] * M for i in range(N)]
    result = 0
    
    
    for i in range(K):
        a, b = map(int, input().split())
        visitable[b][a] = True
    
    for i in range(N):
        for j in range(M):
            if visitable[i][j]:
                DFS(i, j)
                result += 1
    
    print(result)