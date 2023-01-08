from math import gcd
import sys
input = sys.stdin.readline
IP = lambda: map(int, input().split())

def solve():
    N = int(input())
    data = list(IP())
    standard = data[0]
    
    for present in data[1:]:
        GCD = gcd(present, standard)
        print(f"{standard // GCD}/{present // GCD}")
    
if "__main__" == __name__: solve()