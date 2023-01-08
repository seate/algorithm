import sys
input = sys.stdin.readline

def solve():
    def find_parent(searching_num):
        if parent[searching_num] < 0: return searching_num
        parent[searching_num] = find_parent(parent[searching_num])
        return parent[searching_num]
    
    N = int(input())
    M = int(input())
    parent = [-1] * (N + 1)
    
    for i in range(1, N + 1):
        connect = list(map(int, input().split()))
        for j in range(i + 1, N + 1):
            if connect[j - 1]:
                I = find_parent(i)
                J = find_parent(j)
                if I == J: continue
                if parent[I] < parent[J]: parent[I] += parent[J]; parent[J] = I
                else: parent[J] += parent[I]; parent[I] = J
    
    travel_route = list(map(int, input().split()))
    final_parent = find_parent(travel_route[0])
    print("YES" if all(final_parent == find_parent(each) for each in travel_route[1:]) else "NO")

if "__main__" == __name__: solve()