import sys
import heapq
input = sys.stdin.readline
INF = 1e9

def dijkstra(): #특정 조건에서 플로이드 와셜과 비슷한 성능
    Node = int(input())
    path_count = int(input())
    path = [dict() for i in range(Node + 1)]
    
    for i in range(path_count):
        a, b, c = map(int, input().split())
        path[a][b] = (min(path[a][b], c) if b in path[a] else c)
    
    
    for start_node in range(1, Node + 1):
        present_list = [(0, start_node)]
        min_distance = [INF] * (Node + 1)
        min_distance[start_node] = 0
        
        while present_list:
            distance, present_node = heapq.heappop(present_list)
            if distance > min_distance[present_node]: continue
            
            for next_node, next_distance in path[present_node].items():
                next_total_distance = distance + next_distance
                if min_distance[next_node] <= next_total_distance: continue
                min_distance[next_node] = next_total_distance
                heapq.heappush(present_list, (next_total_distance, next_node))
        
        print(' '.join(map(str,[i if i < INF else 0 for i in min_distance[1:]])))

def floyd_warshall():
    Node = int(input())
    path_count = int(input())
    
    dp = [[INF] * (Node + 1) for i in range(Node + 1)]
    for i in range(1, Node + 1): dp[i][i] = 0
    
    for i in range(path_count):
        a, b, c = map(int, input().split())
        if c < dp[a][b]: dp[a][b] = c
    
    for k in range(1, Node + 1):
        for i in range(1, Node + 1):
            for j in range(1, Node + 1):
                tmp = dp[i][k] + dp[k][j]
                if dp[i][j] > tmp: dp[i][j] = tmp
    
    for i in range(1, Node + 1):
        for j in range(1, Node + 1):
            if dp[i][j] == INF: dp[i][j] = 0
    
    for i in range(1, Node + 1): print(*dp[i][1:])
    

if __name__ == "__main__":
    #dijkstra()
    floyd_warshall()