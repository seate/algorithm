import sys
input = sys.stdin.readline
IP = lambda: map(int, input().split())

def solve():
    N = int(input())
    dp = [list(IP()) for i in range(N)]
    
    for i in range(1, N):
        dp[i][0] += dp[i - 1][1] if dp[i - 1][1] < dp[i - 1][2] else dp[i - 1][2]
        dp[i][1] += dp[i - 1][0] if dp[i - 1][0] < dp[i - 1][2] else dp[i - 1][2]
        dp[i][2] += dp[i - 1][0] if dp[i - 1][0] < dp[i - 1][1] else dp[i - 1][1]
    
    print(min(dp[-1]))
    
if "__main__" == __name__: solve()