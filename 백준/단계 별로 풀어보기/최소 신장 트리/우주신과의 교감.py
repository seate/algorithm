import sys
import itertools
import heapq
input = sys.stdin.readline

def solve():
    def find_parent(searching):
        if parent[searching] < 0: return searching
        parent[searching] = find_parent(parent[searching])
        return parent[searching]
    
    def union(a, b):
        A = find_parent(a); B = find_parent(b)
        if A == B: return
        elif A < B: parent[A] += parent[B]; parent[B] = A
        else: parent[B] += parent[A]; parent[A] = B
    
    N, M = map(int, input().split())
    dots = [(None, None)] + [tuple(map(int, input().split())) for i in range(N)]
    parent = [-1] * (N + 1); result = 0; D = []
    
    for i in range(M): union(*map(int, input().split()))
    
    for d1, d2 in itertools.combinations(list(range(1, N + 1)), 2):
        if find_parent(d1) == find_parent(d2): continue
        x1, y1 = dots[d1]
        x2, y2 = dots[d2]
        D.append((((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5, d1, d2))
    
    print(D)
    
    for cost, d1, d2 in sorted(D):
        D1 = find_parent(d1)
        D2 = find_parent(d2)
        if D1 == D2: continue
        union(d1, d2)
        result += cost
    
    print("%.2lf" % result)

def solve2():#half time
    def find_parent(searching):
        if parent[searching] < 0: return searching
        parent[searching] = find_parent(parent[searching])
        return parent[searching]
    
    def union(a, b):
        A = find_parent(a); B = find_parent(b)
        if A == B: return
        elif A < B: parent[A] += parent[B]; parent[B] = A; return parent[A]
        else: parent[B] += parent[A]; parent[A] = B; return parent[B]
    
    N, M = map(int, input().split())
    dots = [tuple(map(int, input().split())) for i in range(N)]
    parent = [-1] * (N + 1); result = 0; D = []
    
    for i in range(M):
        a, b = map(int, input().split())
        a -= 1; b -= 1
        union(a, b)
    
    for d1, d2 in itertools.combinations(list(range(N)), 2):
        if find_parent(d1) == find_parent(d2): continue
        x1, y1 = dots[d1]
        x2, y2 = dots[d2]
        D.append(((((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5, d1, d2)))
    
    heapq.heapify(D); N *= -1
    
    while True:
        cost, d1, d2 = heapq.heappop(D)
        if find_parent(d1) == find_parent(d2): continue
        result += cost
        if union(d1, d2) == N: break
    
    print("%.2lf" % result)

if "__main__" == __name__: solve2()