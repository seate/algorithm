from math import gcd, sqrt
import sys
input = sys.stdin.readline
IP = lambda: map(int, input().split())

def solve():
    N = int(input())
    data = sorted([int(input()) for i in range(N)])
    differs = list({data[i] - data[i - 1] for i in range(1, N)})
    GCD = differs[0]
    
    for i in differs[1:]: GCD = gcd(i, GCD)
    
    result1 = []
    result2 = []
    for i in range(1, int(sqrt(GCD) + 1)):
        if not GCD % i:
            result1.append(i)
            result2.append(GCD // i)
    
    if 1 < len(result1): print(' '.join(map(str, result1[1:])), end = ' ')
    print(' '.join(map(str, result2[::-1])) if result1[-1] != result2[-1] else ' '.join(map(str, result2[-2::-1])))
    
if "__main__" == __name__: solve()