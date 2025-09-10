N, K = map(int, input().split())
v = list(map(int, input().split()))

M = sum(v[:K])
curM = M

for i in range(K, N):
    curM = curM + v[i] - v[i - K]
    
    if M < curM: M = curM

print(M)