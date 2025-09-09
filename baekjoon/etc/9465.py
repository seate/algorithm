import sys
input = sys.stdin.readline
IP = lambda: map(int, input().split())

for _ in range(int(input())):
    N = int(input())
    v = [list(map(int, input().split())) for t in range(2)]
    
    if N <= 1:
        print(max(v[0][0], v[1][0]))
        continue
    elif N <= 2:
        print(max(v[0][0] + v[1][1], v[0][1] + v[1][0]))
        continue
    
    dp = list(v)
    dp[1][1] += dp[0][0]
    dp[0][1] += dp[1][0]
    
    for n in range(2, N):
        # 첫 번째 줄
        dp[0][n] += max([dp[0][n - 2], dp[1][n - 2], dp[1][n - 1]])
        # 두 번째 줄
        dp[1][n] += max([dp[0][n - 2], dp[1][n - 2], dp[0][n - 1]])
    
    print(max(dp[0][n], dp[1][n]))