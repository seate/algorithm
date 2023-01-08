import sys
input = sys.stdin.readline
IP = lambda: map(int, sys.stdin.readline().split())

def solve():
    for i in range(int(input())): print(sum(IP()))
    
if "__main__" == __name__: solve()