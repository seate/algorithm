import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000) 

def DFS(y, x):
    global part_result
    visitable[y][x] = False
    part_result += 1
    
    if y != 0 and visitable[y - 1][x]: DFS(y - 1, x)
    if y != N - 1 and visitable[y + 1][x]: DFS(y + 1, x)
    if x != 0 and visitable[y][x - 1]: DFS(y, x - 1)
    if x != N - 1 and visitable[y][x + 1]: DFS(y, x + 1)
    
N = int(input())
visitable = [list(map(bool, map(int, list(input().rstrip('\n'))))) for i in range(N)]
result = []


for i in range(N):
    for j in range(N):
        if visitable[i][j]:
            part_result = 0
            DFS(i, j)
            result.append(part_result)

print(len(result))
for i in sorted(result): print(i)