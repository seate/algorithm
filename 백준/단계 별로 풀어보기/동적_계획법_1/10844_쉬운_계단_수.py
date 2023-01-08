import sys
input = sys.stdin.readline
IP = lambda: map(int, input().split())

def solve():
    N = int(input())
    dp = [[1] * 10 for i in range(N)]; dp[0][0] = 0
    
    for y in range(1, N):
        dp[y][0] = dp[y - 1][1]
        for x in range(1, 9): dp[y][x] = dp[y - 1][x - 1] + dp[y - 1][x + 1]
        dp[y][9] = dp[y - 1][8]
    
    print(sum(dp[-1]) % 1000000000)
    
if "__main__" == __name__: solve()
