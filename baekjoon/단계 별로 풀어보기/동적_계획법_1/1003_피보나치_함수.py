import sys
input = sys.stdin.readline

def solve():
    query = [int(input()) for T in range(int(input()))]
    dp = [[1, 0], [0, 1]]
    
    for i in range(2, max(query) + 1): dp += [[dp[i - 2][0] + dp[i - 1][0], dp[i - 2][1] + dp[i - 1][1]]]
    
    print("\n".join([' '.join(map(str, dp[q])) for q in query]))
    
if "__main__" == __name__: solve()