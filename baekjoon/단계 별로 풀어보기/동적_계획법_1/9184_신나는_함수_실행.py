import sys
input = sys.stdin.readline
IP = lambda: map(int, input().split())
sys.setrecursionlimit(10 ** 9)

def solve():
    def recur(a, b, c):
        if a <= 0 or b <= 0 or c <= 0: return dp[0][0][0]
        elif 20 < a or 20 < b or 20 < c: return dp[20][20][20]
        
        if dp[a][b][c]: return dp[a][b][c]
        
        if a < b < c: dp[a][b][c] = recur(a, b - 1, c) + recur(a, b, c - 1) - recur(a, b - 1, c - 1)
        else: dp[a][b][c] = recur(a - 1, b, c) + recur(a - 1, b - 1, c) + recur(a - 1, b, c - 1) - recur(a - 1, b - 1, c - 1)
        
        return dp[a][b][c]
    
    dp = [[[0] * 21 for j in range(21)] for i in range(21)]
    dp[0][0][0] = 1; dp[20][20][20] = 1048576
    result = []
    while True:
        a, b, c = IP()
        if a == b == c == -1: break
        result += [f"w({a}, {b}, {c}) = " + str(recur(a, b, c))]
    
    print('\n'.join(result))
    
if "__main__" == __name__: solve()