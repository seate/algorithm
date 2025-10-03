from itertools import combinations

def solution(n, info):
    def combIter():
        I = len(info) - 1
        N = n + I
        
        for a in combinations(range(N), I):
            curComb = []
            
            lastIdx = -1
            
            for aIdx in a:
                curComb.append(aIdx - lastIdx - 1)
                lastIdx = aIdx
            
            curComb.append(N - lastIdx - 1)
            yield curComb
            
            
    def calc(myInfo):
        curResult = [0, 0] # my your
        
        for i in range(len(myInfo)):
            if info[i] == 0 and myInfo[i] == 0: continue
            
            curResult[myInfo[i] <= info[i]] += 10 - i
        
        return curResult[0] - curResult[1]
    
    M = -1
    result= [-1]
    for curInfo in combIter():
        curM = calc(curInfo)
        
        if 0 < curM:
            if M < curM:
                M = curM
                result = curInfo
            elif M == curM: result = sorted([result, curInfo], key=lambda x: x[::-1], reverse=True)[0]
    
    return result