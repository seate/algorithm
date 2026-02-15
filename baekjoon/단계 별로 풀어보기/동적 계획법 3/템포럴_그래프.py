N, T, M = map(int, input().split())
S, E = map(int, input().split())
MAX = 999999999999

edge = [[[] for n in range(N)] for t in range(T)]
for t in range(T):
    for m in range(M):
        a, b, w = map(int, input().split())
        edge[t][a].append([b, w])
        edge[t][b].append([a, w])

dp = [MAX] * N
dp[S] = 0

for t in range(T):
    nxtDp = list(dp)
    
    for cur in range(N):
        for nxt, w in edge[t][cur]:
            nxtDp[nxt] = min(nxtDp[nxt], dp[cur] + w)
    
    dp = list(nxtDp)
            
print(dp[E] if dp[E] != MAX else -1)