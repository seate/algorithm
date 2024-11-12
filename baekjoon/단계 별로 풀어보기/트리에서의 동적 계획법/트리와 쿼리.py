import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

def dfs(present_node):
        dp[present_node] = 1
        for child in connect[present_node]:
            if not dp[child]:
                dfs(child)
                dp[present_node] += dp[child]
    
def Connect(a, b): connect[a].append(b); connect[b].append(a)
    
def initial(N):
    global dp
    global connect
    dp = [0] * (N + 1)
    connect = [[] for _ in range(N + 1)]

def solve():
    N, R, Q = map(int, input().split())
    initial(N)
    
    for _ in range(N - 1):
        a, b = map(int, input().split())
        Connect(a, b)
    
    dfs(R)
    
    for i in (map(int, sys.stdin.readlines())): print(dp[i])

if "__main__" == __name__: solve()