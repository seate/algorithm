import sys
input = sys.stdin.readline
IP = lambda: map(int, input().split())

def solve():
    x, y, w, h = IP()
    print(min(x, y, w - x, h - y))
    
if "__main__" == __name__: solve()