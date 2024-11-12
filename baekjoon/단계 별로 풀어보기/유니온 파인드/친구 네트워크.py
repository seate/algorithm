import sys
input = sys.stdin.readline

def solve():
    def find_parent(searching):
        if parent[searching] == searching: return searching
        parent[searching] = find_parent(parent[searching])
        return parent[searching]
    
    for T in range(int(input())):
        M = int(input())
        parent = dict(); set_size = dict()
        
        for _ in range(M):
            f1, f2 = input().split()
            
            if not f1 in parent: parent[f1] = f1; set_size[f1] = 1
            if not f2 in parent: parent[f2] = f2; set_size[f2] = 1
            
            F1_name = find_parent(f1)
            F2_name = find_parent(f2)
            
            if F1_name == F2_name: print(set_size[F1_name]); continue
            
            if set_size[F1_name] < set_size[F2_name]:
                set_size[F2_name] += set_size[F1_name]
                parent[F1_name] = F2_name
                print(set_size[F2_name])
            
            else:
                set_size[F1_name] += set_size[F2_name]
                parent[F2_name] = F1_name
                print(set_size[F1_name])

if "__main__" == __name__: solve()