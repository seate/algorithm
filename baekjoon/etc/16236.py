from collections import deque

def findNearest(m, startCoord, curSize):
    visit = [[False for x in range(N)] for y in range(N)]
    visit[startCoord[0]][startCoord[1]] = True
    
    q = deque([[startCoord, 0]])
    while True:
        nxtCoords = []
        curAnswers = []
        
        while q:
            cur, dist = q.popleft()
            
            ds = [[-1, 0], [0, -1], [0, 1], [1, 0]]
            for d in ds:
                nxty = cur[0] + d[0]
                nxtx = cur[1] + d[1]
                nxtDist = dist + 1
                
                if (0 <= nxty < N) and (0 <= nxtx < N) and (not visit[nxty][nxtx]) and (m[nxty][nxtx] <= curSize):
                    if 0 < m[nxty][nxtx] < curSize:
                        curAnswers.append([[nxty, nxtx], nxtDist])
                        #return 
                    
                    visit[nxty][nxtx] = True
                    
                    nxtCoords.append([[nxty, nxtx], nxtDist])
        
        if curAnswers:
            return sorted(curAnswers)[0]
        
        if not nxtCoords: break
        
        q = deque(nxtCoords[:])
    
    return None

N = int(input())
m = [list(map(int, input().split())) for _ in range(N)]

cur = None
for y in range(N):
    for x in range(N):
        if m[y][x] == 9:
            cur = [y, x]
            break
    
    if cur: break
m[cur[0]][cur[1]] = 0

answer = 0
curAte = 0
curSize = 2
while True:
    nxts = findNearest(m, cur, curSize)
    if not nxts: break
    
    nxtCur, dist = nxts
    
    m[nxtCur[0]][nxtCur[1]] = 0
    
    answer += dist
    
    curAte += 1
    if curSize == curAte:
        curSize += 1
        curAte = 0
    
    cur = nxtCur

print(answer)