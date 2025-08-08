import collections

N, d, k, c = map(int, input().split())

belt = [int(input()) for _ in range(N)]
cur = collections.defaultdict(int)
for b in belt[:k]: cur[b] += 1


result = len(cur)
idx = 0
while True:
    first = belt[idx]
    last = belt[(idx + k) % N]
    
    cur[first] -= 1
    if (cur[first] == 0): cur.pop(first)
    cur[last] += 1
    
    result = max(result, len(cur) if c in cur else len(cur) + 1)
    
    if (idx := (idx + 1) % N) == 0: break

print(result)