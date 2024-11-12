import sys
input = sys.stdin.readline
IP = lambda: map(int, input().split())

def solve():
    query = [int(input()) for i in range(int(input()))]
    MAX = max(query)
    dp = [1] * (MAX + 1 if 4 < MAX else 6)
    dp[4] = 2; dp[5] = 2
    
    for i in range(6, MAX + 1): dp[i] = dp[i - 1] + dp[i - 5]
    
    print("\n".join(map(str, [dp[q] for q in query])))
    
if "__main__" == __name__: solve()