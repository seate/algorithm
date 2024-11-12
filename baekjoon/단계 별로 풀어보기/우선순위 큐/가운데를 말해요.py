import heapq
import sys
input = sys.stdin.readline
IP = lambda: map(int, input().split())

def solve():
    Mh = []; mh = []; result = []
    for i in range(int(input())):
        command = int(input())
        if i & 1: #min_heap에 넣을 차례
            if command < (Mh[0] * -1):
                temp = command
                command = heapq.heappop(Mh) * -1
                heapq.heappush(Mh, temp * -1)
            heapq.heappush(mh, command)
        
        else: #max_heap에 넣을 차례
            if Mh:
                if mh[0] < command:
                    temp = command
                    command = heapq.heappop(mh)
                    heapq.heappush(mh, temp)
                heapq.heappush(Mh, -1 * command)
            else: Mh.append(command * -1)
        
        result.append(-1 * Mh[0])
    
    print('\n'.join(map(str, result)))
    
if "__main__" == __name__: solve()