from collections import deque

N = int(input())

edge = [[] for _ in range(N + 1)]

while True:
    a, b = map(int, input().split())
    
    if a == -1 and b == -1: break
    
    edge[a].append(b)
    edge[b].append(a)


score = [0] * (N + 1)

for curNode in range(1, N + 1):
    visit = [0] * (N + 1)
    q = deque([curNode])
    
    while len(q) != 0:
        cur = q.popleft()
        
        for nxt in edge[cur]:
            if visit[nxt] != 0 or curNode == nxt: continue
            
            visit[nxt] = visit[cur] + 1
            q.append(nxt)
    
    score[curNode] = max(visit)

minScore = min(score[1:])
cands = []
for i in range(1, N + 1):
    if minScore == score[i]: cands.append(i)
    
print(minScore, len(cands))
print(*cands)