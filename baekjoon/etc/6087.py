from collections import deque
MAX = 999999999999
dy = [1, 0, -1, 0]
dx = [0, -1, 0, 1]

U = 0
L = 1
D = 2
R = 3

nxtDirect = [[L, R], [U, D], [L, R], [U, D]]

X, Y = map(int, input().split())

dp = [[[MAX] * 4 for x in range (X)] for y in range(Y)] # U L D R / count
m = [input() for _ in range(Y)]

se = []
for y in range(Y):
    for x in range(X):
        if m[y][x] == "C": se.append([y, x])
S = se[0]
E = se[1]
dp[S[0]][S[1]] = [0] * 4

q = deque([[*S, i, 0] for i in range(4)]) # y x direct count



while q:
    y, x, direct, cnt = q.popleft()
    
    nxty = y + dy[direct]
    nxtx = x + dx[direct]
        
    if (0 <= nxty and nxty < Y and 0 <= nxtx and nxtx < X) and m[nxty][nxtx] != "*" and cnt < dp[nxty][nxtx][direct]:
        dp[nxty][nxtx][direct] = cnt
        q.append([nxty, nxtx, direct, cnt])
        
    
    for nxtd in nxtDirect[direct]:
        if cnt + 1 < dp[y][x][nxtd]:
            dp[y][x][nxtd] = cnt + 1
            q.append([y, x, nxtd, cnt + 1])
        

print(min(dp[E[0]][E[1]]))