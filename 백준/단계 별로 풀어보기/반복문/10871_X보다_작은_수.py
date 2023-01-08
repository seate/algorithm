import sys
input = sys.stdin.readline
IP = lambda: map(int, sys.stdin.readline().split())

def solve():
    N, X = IP()
    for i in IP():
        if i < X: print(i, end = ' ')
    
if "__main__" == __name__: solve()