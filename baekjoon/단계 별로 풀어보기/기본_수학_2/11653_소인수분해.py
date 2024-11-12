import sys
input = sys.stdin.readline
IP = lambda: map(int, input().split())

def solve():
    N = int(input()); div = 2
    sqrtN = int(N ** 0.5)
    while div <= sqrtN:
        while not N % div:
            print(div)
            N //= div
        div += 1
    if 1 < N: print(N)

if "__main__" == __name__: solve()