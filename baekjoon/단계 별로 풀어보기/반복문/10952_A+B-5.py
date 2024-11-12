import sys
input = sys.stdin.readline
IP = lambda: map(int, sys.stdin.readline().split())

def solve():
    while True:
        a, b = IP()
        if not a and not b: break
        print(a + b)
    
if "__main__" == __name__: solve()