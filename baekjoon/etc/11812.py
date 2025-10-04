import sys
from bisect import bisect_left

input = sys.stdin.readline

IP = lambda: map(int, input().split())


def solve():
    N, K, Q = IP()
    
    if K != 1:
        depthCuts = [1]
        
        i = 1
        while depthCuts[-1] <= N:
            depthCuts.append(depthCuts[-1] + (K ** i))
            i += 1
    


    def getDepth(a): return bisect_left(depthCuts, a + 1)
    def getParent(a): return (a - 1) // K
        
    
    def find(a, b):
        result = 0
        
        ad = getDepth(a)
        bd = getDepth(b)
        
        if ad < bd:
            for i in range(bd - ad):
                b = getParent(b)
            
            result += bd - ad
        else:
            for i in range(ad - bd):
                a = getParent(a)
            
            result += ad - bd
        
        while a != b:
            a = getParent(a)
            b = getParent(b)
            
            result += 2
        
        return result

    for i in range(Q):
        a, b = IP()
        
        a -= 1
        b -= 1
        
        if K != 1:
            print(find(a, b))
        else:
            print(abs(a - b))


if "__main__" == __name__: solve()