import sys
import heapq
import copy
input = sys.stdin.readline
INF = 1e9

def Bellman_Ford():
    Node, path_count = map(int, input().split())
    path = [dict() for i in range(Node + 1)]
    start_node = 1
    min_distance = [INF] * (Node + 1)
    min_distance[start_node] = 0
    
    for i in range(path_count):
        a, b, c = map(int, input().split())
        path[a][b] = (min(path[a][b], c) if b in path[a] else c)
    
    for searching in range(1, Node + 1):
        for present_node in range(1, Node + 1):
            if min_distance[present_node] == INF: continue
            for next_path in path[present_node].items():
                next_node, next_distance = next_path
                if min_distance[present_node] + next_distance < min_distance[next_node]:
                    if searching == Node:
                        print(-1)
                        return
                    
                    min_distance[next_node] = min_distance[present_node] + next_distance
    
    for i in min_distance[2:]: print(i if i != INF else -1)


if __name__ == "__main__":
    Bellman_Ford()