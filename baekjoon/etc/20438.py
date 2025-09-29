IP = lambda: map(int, input().split())

inN, K, Q, M = IP()
N = inN + 3

visit = [False] * N
def check(a):
    ina = a
    while ina < N:
        visit[ina] = True
        ina = ina + a


ks = set(IP())
qs = list(IP())
for q in qs: 
    if q not in ks:
        check(q)

for k in ks: visit[k] = False

dp = [0] * N
for i in range(1, len(visit)): dp[i] = dp[i - 1] + int(not visit[i])

for i in range(M):
    a, b = IP()
    print(dp[b] - dp[a - 1])