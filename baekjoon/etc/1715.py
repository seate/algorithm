import heapq

N = int(input())
h = [int(input()) for _ in range(N)]
heapq.heapify(h)

if N == 1: print(0)
else:
    result = 0
    while len(h) != 1:
        a = heapq.heappop(h)
        b = heapq.heappop(h)
        
        s = a + b
        result += s
        
        heapq.heappush(h, s)
    
    print(result)