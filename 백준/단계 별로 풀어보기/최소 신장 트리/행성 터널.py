import sys
input = sys.stdin.readline

def solve():
    def find_parent(searching):
        if parent[searching] < 0: return searching
        parent[searching] = find_parent(parent[searching])
        return parent[searching]
    
    def union(a, b):
        A = find_parent(a); B = find_parent(b)
        if A == B: return
        elif A < B: parent[A] += parent[B]; parent[B] = A; return parent[A]
        else: parent[B] += parent[A]; parent[A] = B; return parent[B]
    
    N = int(input())
    dots = [(*map(int, input().split()), i) for i in range(N)]
    parent = [-1] * N; result = 0; edges = []
    
    for i in range(3):
        dots.sort(key = lambda x: x[i])
        for j in range(N - 1): edges.append((abs(dots[j][i] - dots[j + 1][i]), dots[j][3], dots[j + 1][3]))
    
    edges.sort(reverse = True); N *= -1
    
    while True:
        cost, d1, d2 = edges.pop()
        if find_parent(d1) == find_parent(d2): continue
        result += cost
        if union(d1, d2) == N: break
    
    print(result)
    
if "__main__" == __name__: solve()