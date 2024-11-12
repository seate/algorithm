from math import factorial
import sys
input = sys.stdin.readline
IP = lambda: map(int, input().split())

def solve():
    dp = [1] * 31
    for i in range(2, 31): dp[i] = dp[i - 1] * i
    
    for T in range(int(input())):
        N, M = IP()
        print(dp[M] // (dp[N] * dp[M - N]))
    
if "__main__" == __name__: solve()