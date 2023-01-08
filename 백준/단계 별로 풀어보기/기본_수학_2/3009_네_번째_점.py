import sys
input = sys.stdin.readline
IP = lambda: map(int, input().split())

def solve():
    x = 0; y = 0
    for i in range(3):
        a, b = IP()
        x ^= a; y ^= b
    print(x, y)
    
if "__main__" == __name__: solve()