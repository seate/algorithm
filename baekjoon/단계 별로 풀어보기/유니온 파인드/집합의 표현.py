import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6 + 5)

def solve():
    def find_parent(searching_num):
        if parent[searching_num] < 0: return searching_num
        parent[searching_num] = find_parent(parent[searching_num])
        return parent[searching_num]
    
    N, M = map(int, input().split())
    parent = [-1] * (N + 1) #맨 위의 부모 노드의 parent[부모 노드] = 항상 -(자식을 갖고있는 수) -> 그러므로 비교해서 적은 쪽을 많은 쪽에 더한다.
    
    for _ in range(M):
        command, a, b = map(int ,input().split())
        if command: print(["NO", "YES"][find_parent(a) == find_parent(b)])
        else:
            A = find_parent(a)
            B = find_parent(b)
            
            if A == B: continue
            
            if parent[A] < parent[B]:
                parent[A] += parent[B]
                parent[B] = A
            else:
                parent[B] += parent[A]
                parent[A] = B
    
if "__main__" == __name__: solve()