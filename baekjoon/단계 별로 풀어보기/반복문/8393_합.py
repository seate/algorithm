import sys
input = sys.stdin.readline
IP = lambda: map(int, sys.stdin.readline().split())

def solve():
    N = int(input())
    print(N * (N + 1) // 2)
    
if "__main__" == __name__: solve()