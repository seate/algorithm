import sys
import heapq
input = sys.stdin.readline

def minimum_length(start_point):
    min_distance = [float("inf")] * (Node + 1)
    min_distance[start_point] = 0
    present_list = [(0, start_point)]
    
    while present_list:
        distance, present_node = heapq.heappop(present_list)
        if distance > min_distance[present_node]: continue
        
        for next_node, next_distance in path[present_node].items():
            next_total_distance = distance + next_distance
            if next_total_distance < min_distance[next_node]:
                min_distance[next_node] = next_total_distance
                heapq.heappush(present_list, (next_total_distance, next_node))
    
    return min_distance


Node, path_count = map(int, input().split())
path = [dict() for i in range(Node + 1)]

for i in range(path_count):
    a, b, c = map(int, input().split())
    if b in path[a]: c = min(path[a][b], c)
    path[a][b] = path[b][a] = c

v1, v2 = map(int, input().split())
v1_start = minimum_length(v1)
v2_start = minimum_length(v2)

result = min(v1_start[1] + v2_start[Node], v1_start[Node] + v2_start[1]) + v1_start[v2]
print(result if result < float("inf") else -1)