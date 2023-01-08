import sys
input = sys.stdin.readline

def solve():
    for T in range(int(input())):
        N = int(input())
        parent = [False] * (N + 1)
        for i in range(N - 1):
            a, b = map(int, input().split())
            parent[b] = a
        t1, t2 = map(int, input().split())
        
        t1_parents = set()
        while t1:
            t1_parents.add(t1)
            t1 = parent[t1]
        
        while not t2 in t1_parents: t2 = parent[t2]
        print(t2)
    
if "__main__" == __name__: solve()