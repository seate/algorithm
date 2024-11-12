input = __import__('sys').stdin.readline
INF = float("inf")

def TSP():
    def recur(last, visited):
        if visited == visited_all: return edge[last][0] or INF
        if cache[last][visited] is not None: return cache[last][visited]
        
        temp = INF
        for city in range(N):
            if visited & (1 << city) == 0 and edge[last][city] != 0: temp = min(temp, recur(city, visited | (1 << city)) + edge[last][city])
        cache[last][visited] = temp
        
        return temp
    
    N = int(input())
    edge = [list(map(int, input().split())) for i in range(N)]
    visited_all = (1 << N) - 1
    cache = [[None] * (1 << N) for i in range(N)]
    return recur(0, 1 << 0)
    
if "__main__" == __name__:
    print(TSP())