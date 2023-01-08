import sys
input = sys.stdin.readline
IP = lambda: map(int, input().split())

def solve():
    N = int(input())
    weight = [int(input()) for i in range(N)]
    dp = [0] * N
    
    dp[0] = weight[0]
    if 2 <= N: dp[1] = weight[0] + weight[1]
    if 3 <= N: dp[2] = (weight[0] if weight[1] < weight[0] else weight[1]) + weight[2]
    
    for i in range(3, N): dp[i] = weight[i] + (dp[i - 2] if dp[i - 3] + weight[i - 1] < dp[i - 2] else dp[i - 3] + weight[i - 1])
    
    print(dp[-1])
    
if "__main__" == __name__: solve()