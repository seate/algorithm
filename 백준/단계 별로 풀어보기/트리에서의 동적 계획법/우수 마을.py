import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 9)
IP = lambda: map(int, input().split())

def solve():
    def dfs(present):
        visit[present] = True; no_dp = 0; yes_dp = weight[present]
        for child in connect[present]:
            if not visit[child]:
                no, yes = dfs(child)
                no_dp += yes
                yes_dp += no
        if yes_dp < no_dp: yes_dp = no_dp
        return no_dp, yes_dp
    
    N = int(input())
    weight = [0, *IP()]
    connect= [[] for i in range(N + 1)]; visit = [False] * (N + 1)
    
    for i in range(N - 1):
        a, b = IP()
        connect[a].append(b); connect[b].append(a)
    
    print(max(dfs(1)))
    
if "__main__" == __name__: solve()