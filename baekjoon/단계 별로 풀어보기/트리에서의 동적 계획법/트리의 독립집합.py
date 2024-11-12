import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

def solve():
    def dfs(present, fir_root, sec_root):
        connect[present].discard(fir_root)
        for child in connect[present]: dfs(child, present, fir_root)
        
        bigger = int(dp[present][0] < dp[present][1])
        
        dp[present] = dp[present][bigger]
        dp[fir_root][0] += dp[present]
        dp[sec_root][1] += dp[present]
        
        trace[present] = trace[present][bigger]
        trace[fir_root][0].add(present)
        trace[sec_root][1].add(present)
    
    
    N = int(input())
    weight = [0, *map(int, input().split()), 0]
    connect = [set() for i in range(N + 1)]
    dp = [[0, weight[i]] for i in range(N + 2)]#[현재 것을 포함하지 않은 것, 포함한 것]
    trace = [[set(), set([i])] for i in range(N + 2)]
    
    
    for i in range(N - 1):
        a, b = map(int, input().split())
        connect[a].add(b); connect[b].add(a)
    
    dfs(1, 0, N + 1)
    
    print(dp[1])
    dp = []
    #for i in range(N): print(i + 1, dp[i + 1], trace[i + 1])
    
    trace_result = set()
    def Trace(present):
        for i in trace[present]: 
            if i != present: Trace(i)
        if present in trace[present]: trace_result.add(present)
    Trace(1)
    print(*sorted(list(trace_result)))
    
def better_solve():
    def dfs(present):
        yes = weight[present]; no = 0
        yes_ele = [present]; no_ele = []
        visit[present] = True
        for child in connect[present]:
            if not visit[child]:
                child_yes, child_no, child_yes_ele, child_no_ele = dfs(child)
                yes += child_no; yes_ele.extend(child_no_ele)
                if child_yes > child_no: no += child_yes; no_ele.extend(child_yes_ele)
                else: no += child_no; no_ele.extend(child_no_ele)
        
        return yes, no, yes_ele, no_ele
    
    
    N = int(input())
    weight = [0, *map(int, input().split())]
    visit = [False] * (N + 1)
    connect = [[] for i in range(N + 1)]
    for i in range(N - 1):
        a, b = map(int, input().split())
        connect[a].append(b); connect[b].append(a)
    
    result_yes, result_no, result_yes_ele, result_no_ele = dfs(1)
    if result_yes > result_no: print(result_yes); print(' '.join(map(str, sorted(result_yes_ele))))
    else: print(result_no); print(' '.join(map(str, sorted(result_no_ele))))
    
if "__main__" == __name__: better_solve()