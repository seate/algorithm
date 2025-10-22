IP = lambda: map(int, input().split())

N, K = IP()
m = [list(IP()) for _ in range(N)]

pieces = []
for _ in range(K):
    temp = list(IP())
    pieces.append([temp[0] - 1, temp[1] - 1, temp[2]])

pieceMap = [[[] for x in range(N)] for y in range(N)]
for p in range(len(pieces)):
    py, px, pm = pieces[p]
    pieceMap[py][px].append(p)


d = [None, [0, 1], [0, -1], [-1, 0], [1, 0]]

answer = -1
for t in range(1, 1001):
    
    for p in range(K):
        py, px, pm = pieces[p]
        pd = d[pm]
        
        nxty = py + pd[0]
        nxtx = px + pd[1]
        curLocationPieces = pieceMap[py][px]
        
        if (not ((0 <= nxty < N) and (0 <= nxtx < N))) or m[nxty][nxtx] == 2:
            if pm == 1: nxtpm = 2
            elif pm == 2: nxtpm = 1
            elif pm == 3: nxtpm = 4
            elif pm == 4: nxtpm = 3
            
            pieces[p][2] = nxtpm
            pd = d[nxtpm]
            
            nxty = py + pd[0]
            nxtx = px + pd[1]
            
            if (not ((0 <= nxty < N) and (0 <= nxtx < N))) or m[nxty][nxtx] == 2: continue
            
        
        if m[nxty][nxtx] == 1:
            idx = curLocationPieces.index(p)
            pieceMap[nxty][nxtx].extend(curLocationPieces[idx:][::-1])
            pieceMap[py][px] = pieceMap[py][px][:idx]
            
            for inp in curLocationPieces[idx:]:
                pieces[inp] = [nxty, nxtx, pieces[inp][2]]
            
        else:
            idx = curLocationPieces.index(p)
            pieceMap[nxty][nxtx].extend(curLocationPieces[idx:])
            pieceMap[py][px] = pieceMap[py][px][:idx]
            
            for inp in curLocationPieces[idx:]:
                pieces[inp] = [nxty, nxtx, pieces[inp][2]]
        
        if 4 <= len(pieceMap[nxty][nxtx]):
            answer = t
            break
    
    if answer != -1: break

print(answer)