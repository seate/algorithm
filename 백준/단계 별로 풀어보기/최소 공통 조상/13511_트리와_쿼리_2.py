from collections import deque
from math import log2
import sys
input = sys.stdin.readline
IP = lambda: map(int, input().split())

def solve():
    def get_cost(a, b):
        result = 0
        if depth[b] < depth[a]: a, b = b, a
        differ = depth[b] - depth[a]
        for i in range(logN):
            if differ & (1 << i):
                result += cost[b][i]
                b = ancestor[b][i]
        
        if a == b: print(result)
        else:
            for i in range(logN - 1, -1, -1):
                if ancestor[a][i] != ancestor[b][i]:
                    result += cost[a][i]
                    result += cost[b][i]
                    a = ancestor[a][i]
                    b = ancestor[b][i]
            
            result += cost[a][0]
            result += cost[b][0]
            print(result)
    
    
    def get_order(initial_start, initial_end, order):
        start = initial_start; end = initial_end
        start_counter = 0; end_counter = 0
        order -= 1
        
        #높이 맞추기
        if depth[start] < depth[end]:
            end, end_counter = adjust_depth(depth[end] - depth[start], end)
        elif depth[end] < depth[start]:
            start, start_counter = adjust_depth(depth[start] - depth[end], start)
        
        #한 쪽이 다른 쪽의 조상이어서 LCA가 이미 구해졌을 때
        if start == end:
            #end가 start의 조상이었을 때
            if end_counter < start_counter: print(get_special_ancestor(order, initial_start))
            #start가 end의 조상이었을 때
            else: print(get_special_ancestor(end_counter - order, initial_end))
        
        #아직 LCA가 구해지지 않았을 때
        else:
            common_counter = 0
            for i in range(logN - 1, -1, -1):
                if ancestor[start][i] != ancestor[end][i]:
                    common_counter += (1 << i)
                    start = ancestor[start][i]
                    end = ancestor[end][i]
            
            start_counter += common_counter + 1
            end_counter += common_counter + 1
            
            #딱 LCA가 order에 해당하는 값이었을 경우
            if order == start_counter: print(ancestor[start][0])
            #start ~ LCA 사이에 order에 해당하는 값이 있을 경우
            elif order < start_counter: print(get_special_ancestor(order, initial_start))
            #LCA ~ end 사이에 order에 해당하는 값이 있을 경우
            elif start_counter < order:
                print(get_special_ancestor(start_counter + end_counter - order, initial_end))
    
    def adjust_depth(differ, a):
        counter = 0
        for i in range(logN):
            if differ & (1 << i):
                counter += (1 << i)
                a = ancestor[a][i]
        return a, counter
    
    def get_special_ancestor(differ, a):
        for i in range(logN):
            if differ & (1 << i): a = ancestor[a][i]
        return a
    
    
    N = int(input())
    logN = int(log2(N)) + 1
    ancestor = [[-1] * logN for i in range(N + 1)]; ancestor[1][0] = 0
    cost = [[0] * logN for i in range(N + 1)]
    depth = [0] * (N + 1)
    edge = [dict() for i in range(N + 1)]
    
    for i in range(N - 1):
        a, b, c = IP()
        edge[a][b] = c; edge[b][a] = c
    
    q = deque([1])
    while q:
        present = q.popleft()
        for i in edge[present]:
            if ancestor[i][0] == -1:
                q.append(i)
                ancestor[i][0] = present
                cost[i][0] = edge[present][i]
                depth[i] = depth[present] + 1
    
    for j in range(1, logN):
        for i in range(1, N + 1):
            ancestor[i][j] = ancestor[ancestor[i][j - 1]][j - 1]
            cost[i][j] = cost[i][j - 1] + cost[ancestor[i][j - 1]][j - 1]
    
    for _ in range(int(input())):
        In = list(IP())
        if In[0] == 1: get_cost(*In[1:])
        else: get_order(*In[1:])
    
if "__main__" == __name__: solve()