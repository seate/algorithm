from math import pi
import sys
input = sys.stdin.readline
IP = lambda: map(int, input().split())

def solve():
    N = int(input()) ** 2
    print(N  * pi, 2 * N, sep = '\n')
    
if "__main__" == __name__: solve()