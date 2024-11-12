import sys
import heapq
input = sys.stdin.readline

def solve():
    vertex, edge = map(int, input().split())
    connect = [dict() for i in range(vertex + 1)]
    
    for i in range(edge):
        a, b, weight = map(int, input().split())
        connect[a][b] = weight; connect[b][a] = weight
    
    visit = [False] * (vertex + 1)
    present = [(0, 1)]; dp = 0
    
    while present:
        present_distance, present_node = heapq.heappop(present)
        if visit[present_node]: continue
        visit[present_node] = True
        dp += present_distance
        
        for next_node in connect[present_node]:
            if not visit[next_node]: heapq.heappush(present, (connect[present_node][next_node], next_node))
    
    print(dp)

def solve2():#better
    def find_parent(searching_num):
        if parent[searching_num] == searching_num: return searching_num
        parent[searching_num] = find_parent(parent[searching_num])
        return parent[searching_num]
    
    vertex, edge = map(int, input().split())
    parent = [i for i in range(vertex + 1)]
    connect = sorted([tuple(map(int, input().split())) for i in range(edge)], key = lambda x: x[2])
    result = 0
    
    for v1, v2, weight in connect:
        if find_parent(v1) == find_parent(v2): continue
        result += weight
        vertex -= 1
        parent[find_parent(v2)] = find_parent(v1)
        if vertex == 1: print(result); break

def solve3():#more better
    def find_parent(searching_num):
        if parent[searching_num] < 0: return searching_num
        parent[searching_num] = find_parent(parent[searching_num])
        return parent[searching_num]
    
    vertex, edge = map(int, input().split())
    parent = [-1] * (vertex + 1); result = 0
    connect = sorted([tuple(map(int, input().split())) for i in range(edge)], key = lambda x: x[2])
    
    for v1, v2, weight in connect:
        V1 = find_parent(v1)
        V2 = find_parent(v2)
        if V1 == V2: continue
        result += weight
        vertex -= 1
        
        if parent[V1] < parent[V2]:
            parent[V1] += parent[V2]
            parent[V2] = V1
            
        else:
            parent[V2] += parent[V1]
            parent[V1] = V2
        
        if vertex == 1: print(result); return

if "__main__" == __name__: solve3()