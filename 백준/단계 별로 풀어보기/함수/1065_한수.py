import sys
input = sys.stdin.readline
IP = lambda: map(int, sys.stdin.readline().split())

def solve():
    def hansu(n):
        L = list(map(int, list(str(n))))
        return bool(L[2] - L[1] == L[1] - L[0])
    
    N = int(input())
    
    if N < 100: print(N)
    elif N == 1000: print(144)
    else:
        count = 99
        
        for i in range(100, N + 1):
            if hansu(i): count += 1
        
        print(count)    
    
if "__main__" == __name__: solve()