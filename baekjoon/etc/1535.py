IP = lambda: map(int, input().split())

N = int(input())
L = list(IP())
J = list(IP())

H = 100

dp = [[0 for h in range(H)] for _ in range(N)]
if L[0] < H: dp[0][L[0]] = J[0]

for i in range(N - 1):
    curCost = L[i + 1]
    curValue = J[i + 1]
    
    for h in range(H):
        if h < curCost: dp[i + 1][h] = dp[i][h]
        else: dp[i + 1][h] = max(dp[i][h], dp[i][h - curCost] + curValue)
    
print(max(dp[N - 1]))