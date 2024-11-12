import sys
input = sys.stdin.readline
IP = lambda: map(int, input().split())

def recursion_solve():
    def recursiondfs(n):
        if n == 0: return 1
        if n <= 2: return n
        return n * recursiondfs(n - 1)
    
    print(recursiondfs(int(input())))

def fastest_solve():
    print([1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880, 3628800, 39916800, 479001600][int(input())])

if "__main__" == __name__:
    #recursion_solve()
    fastest_solve()