import sys
input = sys.stdin.readline
IP = lambda: map(int, sys.stdin.readline().split())

def solve():
    h, m = IP()
    
    if m < 45:
        m += 15
        h -= 1
        if h < 0: h = 23
    else: m -= 45
    
    print(h, m)
    
if "__main__" == __name__: solve()