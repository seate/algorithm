import sys
input = sys.stdin.readline
IP = lambda: map(int, sys.stdin.readline().split())
sys.setrecursionlimit(10 ** 9)

def Kosaraju():
    def forward_dfs(present):
        visited[present] = True
        for next_vertex in forward_edge[present]:
            if not visited[next_vertex]: forward_dfs(next_vertex)
        stack.append(present)
    
    def backward_dfs(present):
        visited[present] = True
        part_scc_set.append(present)
        for next_vertex in backward_edge[present]:
            if not visited[next_vertex]: backward_dfs(next_vertex)
    
    
    V, E = IP()
    forward_edge = [[] for i in range(V + 1)]
    backward_edge = [[] for i in range(V + 1)]
    visited = [False] * (V + 1)
    stack = []; final_scc_set = []
    
    for i in range(E):
        a, b = IP()
        forward_edge[a].append(b)
        backward_edge[b].append(a)
    
    
    for i in range(1, V + 1): forward_edge[i].sort(); backward_edge[i].sort()
    
    for i in range(1, V + 1):
        if not visited[i]: forward_dfs(i)
    
    visited = [False] * (V + 1)
    while stack:
        p = stack.pop()
        if visited[p]: continue
        part_scc_set = []
        backward_dfs(p)
        final_scc_set.append(part_scc_set[:])
    
    for each in final_scc_set: each.sort()
    final_scc_set.sort()
    print(len(final_scc_set))
    for each in final_scc_set: print(' '.join(map(str, each)), end = ' -1\n')
    
    
    
def Tarjan():
    def dfs(present):
        stack.append(present)
        global n
        dfsn[present] = upper[present] = n
        n += 1
        for next_vertex in edge[present]:
            #교차 간선
            if finished[next_vertex]: continue
            #단순 진행
            elif dfsn[next_vertex] < 0:
                temp_up = dfs(next_vertex)
                if temp_up < upper[present]: upper[present] = temp_up
            #역방향 간선
            elif upper[next_vertex] < upper[present]: upper[present] = upper[next_vertex]
        
        #자신으로부터 조상노드로 갈 수 없다면 scc를 추출한다
        if upper[present] == dfsn[present]:
            p = None
            part_scc = []
            while p != present:
                p = stack.pop()
                finished[p] = True
                part_scc.append(p)
            final_scc_set.append(sorted(part_scc))
        
        return upper[present]
    
    
    V, E = IP()
    edge = [[] for i in range(V + 1)]
    dfsn = [-1] * (V + 1)
    upper = [0] * (V + 1)
    finished = [False] * (V + 1)
    stack = []; final_scc_set = []
    global n
    n = 1
    
    for _ in range(E):
        a, b = IP()
        edge[a].append(b)
    
    for i in range(1, V + 1):
        if not finished[i]: dfs(i)
    
    print(len(final_scc_set))
    for each in sorted(final_scc_set): sys.stdout.write(' '.join(map(str, each)) + ' -1\n')
    

if "__main__" == __name__:
    #Kosaraju()
    Tarjan()