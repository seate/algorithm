#웨! 파이썬은! 햄볶칼 수가 업서! 어!!!!!!!!!!!!!!!
#문제 조건 때문에 파이썬 및 파이파이 통과자 0명
#c++로 구현한 결과 소스는 맞음

from collections import deque
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
            #교차간선
            if element_locate[next_vertex] != -1: continue
            #단순진행
            elif dfsn[next_vertex] < 0:
                temp_up = dfs(next_vertex)
                if temp_up < upper[present]: upper[present] = temp_up
            #역방향 간선
            elif upper[next_vertex] < upper[present]: upper[present] = upper[next_vertex]
        
        if upper[present] == dfsn[present]:
            p = None
            present_weight = 0
            present_end = False
            
            while p != present:
                p = stack.pop()
                present_weight += weight[p - 1]
                weight[p - 1] = None
                element_locate[p] = scc_count[0]
                if p in end_point:
                    end_point.remove(p)
                    present_end = True
            
            scc_weight.append(present_weight)
            scc_end_point.append(present_end)
            scc_count[0] += 1
        
        return upper[present]
    
    #입력
    V, E = IP()
    edge = [[] for i in range(V + 1)]
    for i in range(E):
        a, b = IP()
        edge[a].append(b)
    weight = [int(input()) for i in range(V)]
    start, end_count = IP()
    end_point = set(IP())
    
    #dfs 전처리
    dfsn = [-1] * (V + 1)
    upper = [0] * (V + 1)
    stack = []; n = [1]
    
    #dfs 내 scc 전처리
    scc_weight = []
    scc_end_point = []
    scc_count = [0]
    element_locate = [-1] * (V + 1)
    
    #실행
    dfs(start)
    
    del weight
    del dfsn
    del upper
    del end_point
    
    
    
    #========scc순회=============
    #dfs 실행 후 scc순회 전처리
    scc_count = scc_count[0]
    scc_edge = [[] for i in range(scc_count + 1)]
    indegree = [0] * (scc_count + 1)
    scc_max = [0] * (scc_count + 1)
    MAX = 0
    
    start = V
    while start:
        present_edge = edge.pop()
        S = element_locate[start]
        if S != -1:
            while present_edge:
                E = element_locate[present_edge.pop()]
                if S != E and E != -1:
                    scc_edge[S].append(E)
                    indegree[E] += 1
        
        start -= 1
    
    del edge
    
    scc_edge[scc_count].append(scc_count - 1)
    scc_end_point.append(False)
    indegree[scc_count - 1] += 1
    
    
    q = deque([scc_count])
    while q:
        present_locate = q.popleft()
        
        if scc_end_point[present_locate] and MAX < scc_max[present_locate]: MAX = scc_max[present_locate]
        
        for next_vertex in scc_edge[present_locate]:
            next_weight = scc_max[present_locate] + scc_weight[next_vertex]
            if scc_max[next_vertex] < next_weight: scc_max[next_vertex] = next_weight
            
            indegree[next_vertex] -= 1
            if not indegree[next_vertex]: q.append(next_vertex)
    
    print(MAX)
    
if "__main__" == __name__: solve()