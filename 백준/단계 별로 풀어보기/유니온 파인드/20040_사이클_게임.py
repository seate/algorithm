import sys
input = sys.stdin.readline
IP = lambda: map(int, input().split())

def solve():
    def find_parent(search):
        if parent[search] < 0: return search
        parent[search] = find_parent(parent[search])
        return parent[search]
    
    V, E = IP()
    parent = [-1] * V; result = 0
    
    for i in range(E):
        a, b = IP()
        A = find_parent(a); B = find_parent(b)
        if A == B: result = i + 1; break
        elif parent[A] < parent[B]:
            parent[A] += parent[B]
            parent[B] = A
        else:
            parent[B] += parent[A]
            parent[A] = B
    
    print(result)
    
if "__main__" == __name__: solve()