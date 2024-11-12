from math import gcd
import sys
input = sys.stdin.readline
IP = lambda: map(int, input().split())

def solve():
    a, b = IP()
    GCD = gcd(a, b)
    print(GCD)
    print(a * b // GCD)
    
if "__main__" == __name__: solve()