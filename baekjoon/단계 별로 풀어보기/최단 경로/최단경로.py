import sys
import heapq
input = sys.stdin.readline
INF = 1e9

def dijkstra():
    Node, path_count = map(int, input().split())
    start_node = int(input())
    path = [dict() for i in range(Node + 1)]
    min_distance = [INF] * (Node + 1)
    min_distance[start_node] = 0
    present_list = [(0, start_node)]
    
    for i in range(path_count):
        a, b, c = map(int, input().split())
        path[a][b] = (min(path[a][b], c) if b in path[a] else c)
    
    while present_list:
        distance, present_node = heapq.heappop(present_list)
        if distance > min_distance[present_node]: continue
        
        for next_node, next_distance in path[present_node].items():
            next_total_distance = distance + next_distance
            if min_distance[next_node] <= next_total_distance: continue
            min_distance[next_node] = next_total_distance
            heapq.heappush(present_list, (next_total_distance, next_node))
    
    print('\n'.join(map(str,[i if i < INF else "INF" for i in min_distance[1:]])))

if __name__ == "__main__":
    dijkstra()