n, k = map(int, input().split())
dp, dp[0] = [0 for i in range(k + 1)], 1
for i in sorted([int(input()) for i in range(n)]):
    for j in range(i, k + 1): dp[j] += dp[j - i]
print(dp[k])