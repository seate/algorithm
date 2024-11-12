#2-SAT-2과 소스 같음

import sys
input = sys.stdin.readline
IP = lambda: map(int, input().split())
sys.setrecursionlimit(10 ** 9)

def solve():
    def dfs(present):
        stack.append(present)
        dfsn[present] = upper[present] = n[0]
        n[0] += 1
        
        for next_vertex in edge[present]:
            #교차 간선
            if element_locate[next_vertex] != None: continue
            #단순 진행
            elif dfsn[next_vertex] < 0:
                temp_up = dfs(next_vertex)
                if temp_up < upper[present]: upper[present] = temp_up
            #역방향 간선
            elif upper[next_vertex] < upper[present]: upper[present] = upper[next_vertex]
        
        #자신으로부터 조상노드로 갈 수 없다면 scc를 추출한다
        if upper[present] == dfsn[present]:
            p = None
            while p != present:
                p = stack.pop()
                element_locate[p] = scc_count[0]
            scc_count[0] += 1
        
        return upper[present]
    
    N, M = IP()
    edge = [[] for i in range(2 * N + 1)]
    for i in range(M):
        a, b = IP()
        edge[-a].append(b); edge[-b].append(a)
    
    dfsn = [-1] * (2 * N + 1)
    upper = [0] * (2 * N + 1)
    element_locate = [None] * (2 * N + 1)
    stack = []; n = [1]; scc_count = [0]; isit = 1
    #실행
    for i in range(-N, N + 1):
        if element_locate[i] == None: dfs(i)
    
    #검사
    for i in range(1, N + 1):
        if element_locate[i] == element_locate[-i]:
            isit = 0
            break
    
    print(isit)
    
if "__main__" == __name__: solve()