import sys
import heapq
input = sys.stdin.readline
INF = sys.maxsize

def KCM_Travel():
    for T in range(int(input())):
        N, budget, edge_count = map(int, input().split())
        edge = [[] for i in range(N + 1)]
        for i in range(edge_count):
            start, end, cost, distance = map(int, input().split())
            edge[start].append((end, cost, distance))
        
        dp = [[INF] * (budget + 1) for i in range(N + 1)]
        dp[1][0] = 0
        
        present = [(0, 0, 1)] #(time, cost, present_city)
        result = -1
        
        while present:
            time, cost, present_city = heapq.heappop(present)
            if dp[present_city][cost] < time: continue
            if present_city == N:
                result = time
                break
            
            for next_city, next_cost, next_time in edge[present_city]:
                next_time += time
                next_cost += cost
                if budget < next_cost or dp[next_city][next_cost] <= next_time: continue
                for i in range(next_cost, budget + 1):
                    if next_time < dp[next_city][i]: dp[next_city][i] = next_time
                    else: break
                
                heapq.heappush(present, (next_time, next_cost, next_city))
        
        print([result, "Poor KCM"][result == -1])


if "__main__" == __name__:
    KCM_Travel()