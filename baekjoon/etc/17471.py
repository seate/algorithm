IP = lambda: map(int, input().split())
MAX = 9999999999999999999999


N = int(input())
pCounts = [0] + list(IP())
totalPCount = sum(pCounts)

parent = [-1] * (N + 1)
visited = [False] * (N + 1)

edge = [[] for _ in range(N + 1)]
for n in range(1, N + 1): cnt, *edge[n] = IP()
curm = MAX

def dfs(cur, redOrBlue, isornot):
    visited[cur] = True
    
    for nxt in edge[cur]:
        if isornot[nxt] == redOrBlue and findParent(cur) != findParent(nxt):
            union(cur, nxt)
            
            if not visited[nxt]: dfs(nxt, redOrBlue, isornot)


def findParent(a):
    if parent[a] < 0: return a
    parent[a] = findParent(parent[a])
    return parent[a]
    

def union(a, b):
    A = findParent(a)
    B = findParent(b)
    
    if A < B:
        parent[A] += parent[B]
        parent[B] = A
    else:
        parent[B] += parent[A]
        parent[A] = B

def recur(curIdx, isornot):
    if N < curIdx: return
    
    def resetAndGoAndResult():
        #reset
        global parent
        global visited
        parent = [-1] * (N + 1)
        visited = [False] * (N + 1)
        
        #go
        for i in range(1, N + 1):
            dfs(i, isornot[i], isornot)
        
        
        # result
        global curm
        
        rootCnt = sum(1 for p in parent[1:] if p < 0)
    
        if rootCnt == 2:
            redCount = sum(pCounts[i] for i in range(1, N + 1) if isornot[i])
            blueCount = totalPCount - redCount
            
            curm = min(curm, abs(redCount - blueCount))
    
    
    isornot[curIdx] = False
    resetAndGoAndResult()
    recur(curIdx + 1, isornot)
    
    
    #=======
    
    isornot[curIdx] = True
    resetAndGoAndResult()
    recur(curIdx + 1, isornot)
    
    
recur(1, [False] * (N + 1))

print(curm if curm != MAX else -1)