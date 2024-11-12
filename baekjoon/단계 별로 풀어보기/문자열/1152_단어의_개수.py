import sys
input = sys.stdin.readline
IP = lambda: map(int, sys.stdin.readline().split())

def solve(): print(len(input().split()))

if "__main__" == __name__: solve()