import sys
input = sys.stdin.readline
IP = lambda: map(int, input().split())

def solve():
    N, K = IP()
    dp = [1] * (N + 1)
    for i in range(1, N + 1): dp[i] = dp[i - 1] * i
    print(dp[N] // (dp[K] * dp[N - K]))
    
if "__main__" == __name__: solve()