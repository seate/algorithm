import sys
input = sys.stdin.readline
IP = lambda: map(int, sys.stdin.readline().split())

def solve():
    for T in range(int(input())):
        N, alpha = input().split()
        N = int(N)
        for letter in alpha: print(letter * N, end = '')
        print()
    
if "__main__" == __name__: solve()