import sys
import heapq
import itertools
input = sys.stdin.readline

def solve():
    N = int(input())
    dots = []; connect = [dict() for i in range(N)]
    for i in range(N):
        ix, iy = map(float, input().split())
        for j in range(len(dots)):
            jx, jy = dots[j]
            length = ((ix - jx) ** 2 + (iy - jy) ** 2) ** 0.5
            connect[i][j] = length; connect[j][i] = length
        dots.append((ix, iy))
    
    visit = [False] * N
    present = [(0, 0)]; dp = 0
    dots = []
    
    while present:
        present_distance, present_node = heapq.heappop(present)
        if visit[present_node]: continue
        visit[present_node] = True
        dp += present_distance
        
        for next_node in connect[present_node]:
            if not visit[next_node]: heapq.heappush(present, (connect[present_node][next_node], next_node))
    
    print("%.2lf" % dp)
    
def solve2():#similar
    def find_parent(searching_num):
        if parent[searching_num] < 0: return searching_num
        parent[searching_num] = find_parent(parent[searching_num])
        return parent[searching_num]
    
    N = int(input())
    parent = [-1] * (N + 1); D = []; result = 0
    dots = [list(map(float, input().split())) for i in range(N)]
    
    for d1, d2 in itertools.combinations([i for i in range(N)], 2):
        x1, y1 = dots[d1]
        x2, y2 = dots[d2]
        D.append((((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5, d1, d2))
    
    for distance, d1, d2 in sorted(D):
        D1 = find_parent(d1)
        D2 = find_parent(d2)
        if D1 == D2: continue
        
        if D1 < D2:
            parent[D1] += parent[D2]
            parent[D2] = D1
        else:
            parent[D2] += parent[D1]
            parent[D1] = D2
        
        result += distance
    
    print(result)
    
if "__main__" == __name__: solve2()