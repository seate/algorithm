import sys
input = sys.stdin.readline
IP = lambda: map(int, sys.stdin.readline().split())

def solve():
    for i in range(1, int(input()) + 1):
        a, b = IP()
        print(f"Case #{i}: {a + b}")
    
if "__main__" == __name__: solve()