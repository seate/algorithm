import sys
input = sys.stdin.readline
IP = lambda: map(int, sys.stdin.readline().split())

def solve():
    N = int(input())
    for i in range(1, N + 1): print(' ' * (N - i), '*' * i, sep = '')
    
if "__main__" == __name__: solve()