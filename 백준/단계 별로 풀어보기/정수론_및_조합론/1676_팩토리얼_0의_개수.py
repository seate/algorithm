import sys
input = sys.stdin.readline
IP = lambda: map(int, input().split())

def solve():
    N = int(input())
    print(N // 5 + N // 25 + N // 125)
    
if "__main__" == __name__: solve()