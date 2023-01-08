from math import ceil
import sys
input = sys.stdin.readline
IP = lambda: map(int, input().split())

def solve():
    A, B, V = IP()
    print(ceil((V - A) / (A - B)) + 1)
    
if "__main__" == __name__: solve()