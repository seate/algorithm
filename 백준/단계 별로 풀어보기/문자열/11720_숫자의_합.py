import sys
input = sys.stdin.readline
IP = lambda: map(int, sys.stdin.readline().split())

def solve(): input(); print(sum(map(int, input().rstrip())))
    
if "__main__" == __name__: solve()