import collections

MAX = 100000000000

N = int(input())
M = int(input())

tedge = [[MAX] * (N + 1) for _ in range(N + 1)]
for i in range(M):
    st, dest, cost = map(int, input().split())
    
    if cost < tedge[st][dest]: tedge[st][dest] = cost


edge = [[] for _ in range(N + 1)]
for i in range(1, len(tedge)):
    for j in range(len(tedge[i])):
        if tedge[i][j] != MAX:
            edge[i].append([j, tedge[i][j]])

S, D = map(int, input().split())
dq = collections.deque([S])
dp = [MAX] * (N + 1)
dp[S] = 0

while dq:
    cur = dq.popleft()
    
    for nxt, cost in edge[cur]:
        if dp[cur] + cost < dp[nxt]:
            dp[nxt] = dp[cur] + cost
            dq.append(nxt)

print(dp[D])