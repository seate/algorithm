class block:
    def __init__(self, y, x, blockMap):
        self.y = y
        self.x = x
        self.blockMap = blockMap
    
    def getNum(self, m, starty, startx):
        result = 0
        
        for y in range(self.y):
            for x in range(self.x):
                my = starty + y
                mx = startx + x
                
                if self.blockMap[y][x]:
                    result += m[my][mx]
        
        return result
                
            
        
def getSepa(blockMap):
    def rotate(blockMap):
        Y = len(blockMap)
        X = len(blockMap[0])
        
        nBlockMap = [[False] * Y for _ in range(X)]
        
        for y in range(Y):
            for x in range(X):
                nBlockMap[x][Y - 1 - y] = blockMap[y][x]
        
        return nBlockMap

    
    def upend(blockMap):
        Y = len(blockMap)
        X = len(blockMap[0])
        
        nBlockMap1 = []
        nBlockMap2 = []
        for row in blockMap:
            nBlockMap1.append(row[:])
            nBlockMap2.append(row[:])
        
        for y in range(Y):
            for x in range(X):
                nBlockMap1[y][X - 1 - x] = blockMap[y][x]
                nBlockMap2[Y - 1 - y][x] = blockMap[y][x]
        
        return [nBlockMap1, nBlockMap2]        
    
    sepas = []
    curBlockMap = blockMap[:]    
    for i in range(3):
        curBlockMap = rotate(curBlockMap)
        upend1, upend2 = upend(curBlockMap)
        sepas.append(curBlockMap[:])
        sepas.append(upend1)
        sepas.append(upend2)
    
        
    result = []
    for s in sepas:
        Y = len(s)
        X = len(s[0])
        
        result.append([Y, X, s])
        
    return result


Y, X = map(int, input().split())
m = [list(map(int, input().split())) for y in range(Y)]

blocks = [
    block(1, 4, [[True, True, True, True]]),
    block(4, 1, [[True] for _ in range(4)]),
    block(2, 2, [[True for x in range(2)] for y in range(2)])
]

asdf = [
    [3, 2, [
        [True, False],
        [True, False],
        [True, True],
    ]],
    [3, 2, [
        [True, False],
        [True, True],
        [False, True],
    ]],
    [3, 2, [
        [True, False],
        [True, True],
        [True, False],
    ]]
]

for y, x, bm in asdf:
    blocks.append(block(y, x, bm))
    
    for s in getSepa(bm):
        blocks.append(block(*s))

answer = 0
for curBlock in blocks:
    a =3
    for y in range(Y - curBlock.y + 1):
        for x in range(X - curBlock.x + 1):
            answer = max(answer, curBlock.getNum(m, y, x))

print(answer)
    
    
    