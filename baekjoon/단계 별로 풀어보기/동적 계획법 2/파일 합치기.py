import sys
input = sys.stdin.readline


for n in range(int(input())):
    K = int(input())
    files = list(map(int, input().split()))
    dp = [[0] * K for j in range(K)]
    knuth = [[0] * K for j in range(K)]
    S = [0] * (K + 1)
    S[1] = files[0]
    
    for j in range(K):
        S[j + 1] = S[j] + files[j]
        knuth[j][j] = j
    
    for x in range(1, K):
        for i in range(K - x):
            j = i + x
            dp[i][j] = 999999999999
            
            for k in range(knuth[i][j - 1], knuth[i + 1][j] + 1):
                if k < K - 1 and dp[i][j] > dp[i][k] + dp[k + 1][j] + S[j + 1] - S[i]:
                    dp[i][j] = dp[i][k] + dp[k + 1][j] + S[j + 1] - S[i]
                    knuth[i][j] = k
    
    print(dp[0][K - 1])