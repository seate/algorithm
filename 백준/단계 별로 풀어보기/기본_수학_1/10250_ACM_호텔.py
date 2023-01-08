from math import ceil
import sys
input = sys.stdin.readline
IP = lambda: map(int, input().split())

def solve():
    for T in range(int(input())):
        H, trash, N = IP()
        print(str((N - 1) % H + 1) + str((N - 1) // H + 1).rjust(2, "0"))
    
if "__main__" == __name__: solve()