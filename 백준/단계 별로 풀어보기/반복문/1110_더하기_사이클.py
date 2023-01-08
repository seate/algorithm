import sys
input = sys.stdin.readline
IP = lambda: map(int, sys.stdin.readline().split())

def solve():
    N = int(input())
    n = (((N // 10) + (N % 10)) % 10) + ((N % 10) * 10)
    count = 1
    while N != n:
        n = (((n // 10) + (n % 10)) % 10) + ((n % 10) * 10)
        count += 1
    print(count)
    
if "__main__" == __name__: solve()