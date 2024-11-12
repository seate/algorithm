import sys
import heapq
input = sys.stdin.readline
INF = sys.maxsize

def solve():
    def find_path(present):
        while present:
            present_cost, present_city = heapq.heappop(present)
            if dp[present_city] < present_cost: continue
            
            for next_city, next_cost in edge[present_city].items():
                next_cost += present_cost
                if dp[next_city] > next_cost:
                    dp[next_city] = next_cost
                    Trace[next_city] = present_city
                    heapq.heappush(present, (next_cost, next_city))
        
        return dp[destination]
    
    N = int(input()); M = int(input())
    edge = [dict() for i in range(N + 1)]
    for i in range(M):
        start, end, cost = map(int, input().split())
        edge[start][end] = cost if not end in edge[start] else min(edge[start][end], cost)
    departure, destination = map(int, input().split())
    
    Trace = [False] * (N + 1)
    dp = [INF] * (N + 1)
    dp[departure] = 0
    
    print(find_path([(0, departure)]))
    
    result_trace = []
    while destination: result_trace.append(destination); destination = Trace[destination]
    
    print(len(result_trace))
    print(' '.join(map(str, result_trace[::-1])))
    
if "__main__" == __name__: solve()