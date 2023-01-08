import sys
input = sys.stdin.readline
IP = lambda: map(int, sys.stdin.readline().split())

def solve():
    a, b = int(input()), int(input())
    print(a * (b % 10), a * ((b // 10) % 10), a * (b // 100), a * b, sep = '\n')
    
if "__main__" == __name__: solve()