import sys
input = sys.stdin.readline
IP = lambda: map(int, input().split())

def recursion_solve():
    def fibonacci(n):
        if n <= 2: return 1
        return fibonacci(n - 1) + fibonacci(n - 2)
    
    N = int(input())
    print(fibonacci(N) if N else '0')

def fastest_solve():
    print([0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765][int(input())])
    
if "__main__" == __name__:
    #recursion_solve()
    fastest_solve()