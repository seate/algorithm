import sys
input = sys.stdin.readline
IP = lambda: map(int, input().split())

def solve():
    N, MAX = IP()
    dp = [[0] * (MAX + 1) for i in range(N + 1)]
    data = [list(IP()) for i in range(N)]
    data.sort(key = lambda x: x[1])
    data.sort(key = lambda x: x[0])
    
    for i in range(1, N + 1):
        for j in range(1, MAX + 1):
            if data[i - 1][0] <= j: dp[i][j] = dp[i - 1][j] if data[i - 1][1] + dp[i - 1][j - data[i - 1][0]] < dp[i - 1][j] else data[i - 1][1] + dp[i - 1][j - data[i - 1][0]]
            else: dp[i][j] = dp[i - 1][j]
    
    print(dp[N][MAX])
    
if "__main__" == __name__: solve()