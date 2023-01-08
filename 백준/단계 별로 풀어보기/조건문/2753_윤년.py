import sys
input = sys.stdin.readline
IP = lambda: map(int, sys.stdin.readline().split())

def solve():
    a = int(input())
    if not a % 400: print(1)
    elif not a % 100: print(0)
    elif not a % 4: print(1)
    else: print(0)
    
if "__main__" == __name__: solve()