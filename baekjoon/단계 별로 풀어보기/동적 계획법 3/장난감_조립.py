from collections import defaultdict

N = int(input())
M = int(input())

req = [defaultdict(int) for _ in range(N + 1)]
for i in range(M):
    a, b, c = map(int, input().split())
    req[a][b] += c

def recur(cur, curCnt):
    if not req[cur]: return {cur : curCnt}

    curResult = defaultdict(int)
    for nxt, nxtCnt in req[cur].items():
        for res, resCnt in recur(nxt, nxtCnt).items():
            curResult[res] += resCnt
    req[cur] = curResult
    
    return {i: (cnt * curCnt) for i, cnt in curResult.items()}

for n, cnt in sorted(list(recur(N, 1).items())): print(n, cnt)