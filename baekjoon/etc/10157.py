X, Y = map(int, input().split())
K = int(input())

if X * Y < K: print(0)
else:
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    
    m = [[False] * X for _ in range(Y)]
    
    cur = 1
    curDI = 0
    curx, cury = 0, 0
    
    while cur < K:
        nxty = cury + dy[curDI]
        nxtx = curx + dx[curDI]
        if Y <= nxty or X <= nxtx or m[nxty][nxtx]:
            curDI = (curDI + 1) % 4
            continue
        
        m[cury][curx] = True
        
        cur += 1
        cury = nxty
        curx = nxtx
    
    print(curx + 1, cury + 1)