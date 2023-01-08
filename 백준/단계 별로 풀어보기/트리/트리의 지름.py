import sys
import collections
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6 + 100)

MAX = 0
def Top_down():
    V = int(input())
    Tree = [dict() for i in range(V + 1)]
    dp = [0] * (V + 1)
    visited = [False] * (V + 1); visited[1] = True
    
    for i in range(V):
        vertex, *edge = list(map(int, input().split()[:-1]))
        for j in range(0, len(edge) - 1, 2):
            if not edge[j] in Tree[vertex]: Tree[vertex][edge[j]] = edge[j + 1]
            if not vertex in Tree[edge[j]]: Tree[edge[j]][vertex] = edge[j + 1]
    
    def DFS(present_vertex):
        global MAX
        
        for child in Tree[present_vertex].keys():
            if visited[child]: continue
            visited[child] = True
            temp = DFS(child) + Tree[present_vertex][child]
            if dp[present_vertex] and MAX < dp[present_vertex] + temp: MAX = dp[present_vertex] + temp
            if dp[present_vertex] < temp: dp[present_vertex] = temp
        return dp[present_vertex]
    
    DFS(1)
    print(max(max(dp), MAX))

def Bottom_up():
    V = int(input())
    terminals = collections.deque([])
    weight = [dict() for i in range(V + 1)]
    edge_count = [0] * (V + 1); dp = [0] * (V + 1); MAX = 0
    
    for i in range(V):
        vertex, *edge = list(map(int, input().split()[:-1]))
        edge_count[vertex] = len(edge) // 2
        if edge_count[vertex] == 1: terminals.append(vertex)
        for j in range(0, edge_count[vertex] * 2, 2):
            weight[vertex][edge[j]] = edge[j + 1]
            weight[edge[j]][vertex] = edge[j + 1]
    
    while terminals:
        terminal = terminals.pop()
        for next_vertex in weight[terminal].keys():
            if not edge_count[next_vertex]: continue
            
            present_weight_sum = dp[terminal] + weight[terminal][next_vertex]
            
            if MAX < dp[next_vertex] + present_weight_sum: MAX = dp[next_vertex] + present_weight_sum
            
            if dp[next_vertex] < present_weight_sum: dp[next_vertex] = present_weight_sum
            
            edge_count[terminal] -= 1; edge_count[next_vertex] -= 1
            if edge_count[next_vertex] == 1: terminals.append(next_vertex)
    
    print(max(max(dp), MAX))
    
if "__main__" == __name__:
    Top_down()#이게 더 빠름
    #Bottom_up()