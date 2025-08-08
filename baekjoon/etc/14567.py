IP = lambda: map(int, input().split())

N, K = IP()

before = [[] for _ in range(N + 1)]
for i in range(K):
    bef, cur = IP()
    before[cur].append(bef)

result = [1] * (N + 1)
for curIdx in range(1, N + 1):
    for bef in before[curIdx]:
        result[curIdx] = max(result[curIdx], result[bef] + 1)

print(" ".join(map(str, result[1:])))