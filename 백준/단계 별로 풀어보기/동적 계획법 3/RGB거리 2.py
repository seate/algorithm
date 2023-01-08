import sys
import copy
input = sys.stdin.readline

def each_cost(dp, first_idx):
    temp = [0, 1, 2]
    temp.pop(first_idx)
    
    for i in temp: dp[1][i] += dp[0][first_idx]
    
    if 3 <= N:
        for i in range(3):
            if i == first_idx: dp[2][first_idx] += min(dp[1][temp[0]], dp[1][temp[1]])
            
            else:
                for j in temp:
                    if i != j: dp[2][i] += dp[1][j]
    
    for i in range(3, N):
        dp[i][0] += min(dp[i - 1][1], dp[i - 1][2])
        dp[i][1] += min(dp[i - 1][0], dp[i - 1][2])
        dp[i][2] += min(dp[i - 1][0], dp[i - 1][1])
    
    return min(dp[N - 1][temp[0]], dp[N - 1][temp[1]])
    


N = int(input())
costs = [list(map(int, input().split())) for i in range(N)]
result = [each_cost(copy.deepcopy(costs), i) for i in range(3)]
print(min(result))