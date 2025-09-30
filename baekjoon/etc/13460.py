from collections import deque
MAX = 999999999999
U = 0
L = 1
D = 2
R = 3
# U L D R
dy = [1, 0, -1, 0]
dx = [0, -1, 0, 1]

Y, X = map(int, input().split())

m = [list(input()) for _ in range(Y)]

RED = None
BLUE = None
GOAL = None

for y in range(Y):
    for x in range(X):
        if m[y][x] == "R": 
            RED = [y, x]
            m[y][x] = "."
        elif m[y][x] == "B":
            BLUE = [y, x]
            m[y][x] = "."
        elif m[y][x] == "O": GOAL = [y, x]


def getNext(y, x, othery, otherx, direct):
    nxty = y + dy[direct]
    nxtx = x + dx[direct]
    
    goalIn = False
    
    while (0 <= nxty and nxty < Y and 0 <= nxtx and nxtx < X) and m[nxty][nxtx] != "#" and not (nxty == othery and nxtx == otherx):
        if nxty == GOAL[0] and nxtx == GOAL[1]:
            goalIn = True
            break
        
        nxty += dy[direct]
        nxtx += dx[direct]
    
    return [nxty -  dy[direct], nxtx - dx[direct], goalIn]

result = MAX
q = deque([[*RED, *BLUE, 0]]) # ry, rx, by, bx, cnt
found = False
s = set()

while q:
    ry, rx, by, bx, cnt = q.popleft()
    
    if 10 <= cnt: continue
    
    isRFirst = [by < ry, rx < bx, ry < by, bx < rx]
    
    for direct in range(4):
        if isRFirst[direct]:
            nxtry, nxtrx, rgoal = getNext(ry, rx, by, bx, direct)
            
            if rgoal:
                nxtry = Y + 10
                nxtrx = X + 10
            
            nxtby, nxtbx, bgoal = getNext(by, bx, nxtry, nxtrx, direct)
            
            if bgoal: continue
            
            if rgoal:
                result = cnt + 1
                found = True
                break
            
            else:
                k = ''.join(map(str, [nxtry, nxtrx, nxtby, nxtbx]))
                if k in s: continue
                s.add(k)
                
                q.append([nxtry, nxtrx, nxtby, nxtbx, cnt + 1])
        
        else:
            nxtby, nxtbx, bgoal = getNext(by, bx, ry, rx, direct)
            
            if bgoal: continue
            
            nxtry, nxtrx, rgoal = getNext(ry, rx, nxtby, nxtbx, direct)
            
            if rgoal:
                result = cnt + 1
                found = True
                break
            
            else:
                k = ''.join(map(str, [nxtry, nxtrx, nxtby, nxtbx]))
                if k in s: continue
                s.add(k)
                
                q.append([nxtry, nxtrx, nxtby, nxtbx, cnt + 1])
    
    if found: break

print(result if result != MAX else -1)