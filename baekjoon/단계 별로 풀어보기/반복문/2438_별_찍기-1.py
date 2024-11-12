import sys
input = sys.stdin.readline
IP = lambda: map(int, sys.stdin.readline().split())

def solve():
    for i in range(1, int(input()) + 1): print('*' * i)
    
if "__main__" == __name__: solve()