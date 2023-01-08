import sys
input = sys.stdin.readline
IP = lambda: map(int, input().split())
sys.setrecursionlimit(10 ** 9)

def solve():
    def dfs(present):
        stack.append(present)
        global n
        dfsn[present] = upper[present] = n
        n += 1
        
        for next_vertex in edge[present]:
            if finished[next_vertex]: continue
            elif dfsn[next_vertex] < 0:
                temp_up = dfs(next_vertex)
                if temp_up < upper[present]: upper[present] = temp_up
            elif upper[next_vertex] < upper[present]:
                upper[present] = upper[next_vertex]
        
        if upper[present] == dfsn[present]:
            p = None
            part_scc = []
            while p != present:
                p = stack.pop()
                finished[p] = True
                part_scc += [p]
            final_scc_set.append(part_scc)
        
        return upper[present]
    
    for T in range(int(input())):
        V, E = IP()
        edge = [[] for i in range(V)]
        dfsn = [-1] * V
        upper = [0] * V
        finished = [False] * V
        parent = [-1] * V
        stack = []
        final_scc_set = []
        global n
        n = 1
        
        
        for i in range(E):
            a, b = IP()
            edge[a] += [b]
        
        for i in range(V):
            if not finished[i]: dfs(i)
        
        indegree = [0] * len(final_scc_set)
        
        for index, each_scc in enumerate(final_scc_set):
            for scc_element in each_scc:
                parent[scc_element] = index
        
        
        for i in range(V):
            for j in edge[i]:
                if parent[i] != parent[j]: indegree[parent[j]] = 1
        
        result = indegree.count(0)
        print('\n'.join(map(str, sorted(final_scc_set[indegree.index(0)]))) if result < 2 else "Confused")
        print()
        input()
    
if "__main__" == __name__: solve()