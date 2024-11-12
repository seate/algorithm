import sys
import heapq
input = sys.stdin.readline
INF = int(1e9)

def solve():
    for T in range(int(input())):
        Node, path_count, destination_candidate_count = map(int, input().split())
        start_node, v1, v2 = map(int, input().split())
        path = [dict() for i in range(Node + 1)]
        min_distance = [INF] * (Node + 1)
        min_distance[start_node] = 0
        present_list = [(0, start_node)]
        
        for i in range(path_count):
            a, b, c = map(int, input().split())
            path[a][b] = c
            path[b][a] = c
        
        path[v1][v2] -= 0.1
        path[v2][v1] -= 0.1
        
        destination_candidate = {int(input()) for i in range(destination_candidate_count)}
        
        while present_list:
            distance, present_node = heapq.heappop(present_list)
            if distance > min_distance[present_node]: continue
            
            for next_node, next_distance in path[present_node].items():
                next_total_distance = distance + next_distance
                if min_distance[next_node] <= next_total_distance: continue
                min_distance[next_node] = next_total_distance
                heapq.heappush(present_list, (next_total_distance, next_node))
        
        for i in sorted(destination_candidate):
            if type(min_distance[i]) == float: print(i, end = ' ')
        print()

if __name__ == "__main__":
    solve()