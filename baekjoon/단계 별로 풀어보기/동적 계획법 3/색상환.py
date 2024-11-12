import sys
input = sys.stdin.readline

def solve():
    N = int(input())
    K = int(input())
    if N < 2 * K: return 0
    if K == 1: return N
    
    dp = [[0] * (K + 1) for i in range(N + 1)]
    
    for n in range(1, N - 2 * K + 3): dp[n][1] = n
    
    for k in range(2, K + 1):
        for n in range(2 * k - 1, (N + 1) + 2 * (k - K)): dp[n][k] = dp[n - 2][k - 1] + dp[n - 1][k]
    
    return (dp[N][K] - (dp[N - 4][K - 2] if K - 2 else 1)) % 1000000003
    
if __name__ == "__main__":
    print(solve())