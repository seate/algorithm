import sys
input = sys.stdin.readline
IP = lambda: map(int, sys.stdin.readline().split())

def solve():
    remain = [False] * 42
    for i in range(10): remain[int(input()) % 42] = True
    print(sum(remain))
    
if "__main__" == __name__: solve()