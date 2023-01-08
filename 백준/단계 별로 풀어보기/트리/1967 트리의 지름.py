import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6 + 100)
MAX = 0

def solve():
    V = int(input())
    dp = [0] * (V + 1); candidate = set(range(1, V + 1))
    
    Tree = [dict() for i in range(V + 1)]
    for i in range(V - 1):
        p, c, w = map(int, input().split())
        Tree[p][c] = w
        candidate.discard(c)
    
    def DFS(present_vertex):
        global MAX
        
        for child in Tree[present_vertex].keys():
            temp = DFS(child) + Tree[present_vertex][child]
            if dp[present_vertex] and MAX < dp[present_vertex] + temp: MAX = dp[present_vertex] + temp
            if dp[present_vertex] < temp: dp[present_vertex] = temp
        return dp[present_vertex]
    
    DFS(list(candidate)[0])
    print(max(max(dp), MAX))

if "__main__" == __name__: solve()