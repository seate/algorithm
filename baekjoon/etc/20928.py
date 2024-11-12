import sys
input = sys.stdin.readline
IP = lambda: map(int, input().split())

NOT_VISITED = 9999999

def solve():
    pointCount, dest = IP()
    
    points = list(IP())
    maxJump = list(IP())
    
    minCount = [NOT_VISITED] * pointCount
    minCount[0] = 0
    
    curMax = 0
    curidx = 0
    maxidx = 1
    while True:
        if (pointCount <= curidx) or (minCount[curidx] == NOT_VISITED):
            print(-1)
            return
        
        nextMax = points[curidx] + maxJump[curidx]
        
        if nextMax <= curMax:
            curidx += 1
            continue
        
        if dest <= nextMax:
            print(minCount[curidx])
            return
        
        curMax = nextMax
        for nxtidx in range(maxidx, pointCount):
            if not (points[nxtidx] <= nextMax): break
                
            minCount[nxtidx] = minCount[curidx] + 1
            maxidx = nxtidx + 1
    
    
            
    
    
    
if "__main__" == __name__: solve()