import sys
input = sys.stdin.readline
IP = lambda: map(int, sys.stdin.readline().split())

def solve():
    a, b = int(input()), int(input())
    print([[3, 2], [4, 1]][0 < a][0 < b])
    
if "__main__" == __name__: solve()