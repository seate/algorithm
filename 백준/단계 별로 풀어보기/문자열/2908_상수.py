import sys
input = sys.stdin.readline
IP = lambda: map(int, sys.stdin.readline().split())

def solve():
    a, b = input().split()
    a = int(a[::-1]); b = int(b[::-1])
    print(a if b < a else b)

if "__main__" == __name__: solve()