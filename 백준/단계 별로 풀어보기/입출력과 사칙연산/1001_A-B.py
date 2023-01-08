import sys
input = sys.stdin.readline
IP = lambda: map(int, sys.stdin.readline().split())

def solve():
    a, b = IP()
    print(a - b)

if "__main__" == __name__: solve()