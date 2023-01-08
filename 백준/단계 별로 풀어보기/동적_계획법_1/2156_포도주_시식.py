import sys
input = sys.stdin.readline
IP = lambda: map(int, input().split())

def solve():
    N = int(input())
    weight = [int(input()) for i in range(N)]
    if N < 3:
        if N == 1: print(weight[0])
        else: print(weight[0] + weight[1])
        return
    
    dp = [0] * N
    dp[0] = weight[0]
    dp[1] = weight[0] + weight[1]
    dp[2] = dp[1] + weight[2] - min(weight[:3])
    for i in range(3, N):
        temp = (dp[i - 3] + weight[i - 1] if dp[i - 2] < dp[i - 3] + weight[i - 1] else dp[i - 2]) + weight[i]
        dp[i] = temp if dp[i - 1] < temp else dp[i - 1]
    
    print(dp[-1])
    
if "__main__" == __name__: solve()