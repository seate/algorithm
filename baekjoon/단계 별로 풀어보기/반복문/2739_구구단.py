import sys
input = sys.stdin.readline
IP = lambda: map(int, sys.stdin.readline().split())

def solve():
    N = int(input())
    for i in range(1, 10): print(N, '*', i, '=', N * i)
    
if "__main__" == __name__: solve()