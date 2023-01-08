import sys
input = sys.stdin.readline
IP = lambda: map(int, sys.stdin.readline().split())

def solve():
    N = int(input())
    score = list(IP())
    print(sum(score) / max(score) * 100 / N)
    
if "__main__" == __name__: solve()