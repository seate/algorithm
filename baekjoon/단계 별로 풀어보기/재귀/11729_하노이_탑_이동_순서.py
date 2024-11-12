import sys
input = sys.stdin.readline
IP = lambda: map(int, input().split())

def solve():
    def recursion(n, a, b, c):
        if n == 1: print(a, c)
        else:
            recursion(n - 1, a, c, b)
            print(a, c)
            recursion(n - 1, b, a, c)
    
    N = int(input())
    print(2 ** N - 1)
    recursion(N, 1, 2, 3)
    
if "__main__" == __name__: solve()