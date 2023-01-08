import sys
import heapq
import collections
input = sys.stdin.readline
INF = 1e9

def floyd_warshall():
    Node, path_count = map(int, input().split())
    dp = [[INF] * (Node + 1) for i in range(Node + 1)]
    for i in range(path_count):
        a, b, c = map(int, input().split())
        dp[a][b] = c
    
    for k in range(1, Node + 1):
        for i in range(1, Node + 1):
            for j in range(1, Node + 1):
                tmp = dp[i][k] + dp[k][j]
                if dp[i][j] > tmp: dp[i][j] = tmp
    
    result = INF
    for i in range(1, Node + 1): result = min(result, dp[i][i])
    print(result if result != INF else -1)


def solve(): #왜인지는 모르겠는데 이 풀이만 함수 호출 형식으로 하면 시간이 2배 이상으로 늘어남. 아닐 경우 이 풀이 시간 * 2 == floyd_warshall 시간
    Node, path_count = map(int, input().split())
    path = collections.defaultdict(list)
    
    for i in range(path_count):
        a, b, c = map(int, input().split())
        path[a].append((b, c))
    
    ans = sys.maxsize
    que = collections.deque()
    for k in path.keys(): que.append((k, k, 0))
    
    while que:
        present_node, destination, distance = que.popleft()
        for next_node, next_distance in path[present_node]:
            if distance + next_distance >= ans: continue
            if next_node == destination: ans = distance + next_distance
            else: que.append((next_node, destination, distance + next_distance))
    
    print(ans if ans != sys.maxsize else -1)


if __name__ == "__main__":
    #floyd_warshall()
    solve()