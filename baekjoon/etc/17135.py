from collections import deque
from itertools import combinations

IP = lambda: map(int, input().split())

def findEnemy(m, curx):
    Y = len(m)
    X = len(m[0])
    
    visit = [[False] * X for y in range(Y)]
    
    cury = Y - 1
    
    q = deque()
    q.append([cury, curx, 1])
    visit[cury][curx] = True
    
    while q:
        y, x, d = q.popleft()
        
        if m[y][x]: return [y, x]
        
        nxts = [[y, x - 1], [y - 1, x], [y, x + 1]]
        for nxty, nxtx in nxts:
            if 0 <= nxty < Y and 0 <= nxtx < X and not visit[nxty][nxtx] and d + 1 <= D:
                q.append([nxty, nxtx, d + 1])
    
    return None
            
        
def filt(l):
    return set(tuple(a) for a in l)


Y, X, D = IP()
m = [list(IP()) for y in range(Y)]

answer = 0
for arches in list(combinations(list(range(X)), 3)):
    curAnswer = 0
    inm = [i[:] for i in m]
    
    for t in range(Y):        
        filteredEnemies = []
        for arch in arches:
            curResult = findEnemy(inm, arch)
            if not curResult: continue
            
            filteredEnemies.append(curResult)
        filteredEnemies = filt(filteredEnemies)
        
        for enemy in filteredEnemies: inm[enemy[0]][enemy[1]] = 0
        
        curAnswer += len(filteredEnemies)
        
        #move down
        for y in range(Y - 1, -1, -1): inm[y] = inm[y - 1][:]
        inm[0] = [0] * X
    
    answer = max(answer, curAnswer)

print(answer)