import sys
input = sys.stdin.readline
IP = lambda: map(int, input().split())

def solve():
    print('\n'.join(map(str, sorted([int(input()) for i in range(int(input()))]))))
    
if "__main__" == __name__: solve()