import sys
import collections
input = sys.stdin.readline

#아무 생각없이 문제를 풀었을 때
def solve():
    for T in range(int(input())):
        N, M = map(int, input().split())
        connect = [[] for i in range(N + 1)]
        for i in range(M):
            a, b = map(int, input().split())
            connect[a].append(b); connect[b].append(a)
        
        visit = [False] * (N + 1); visit[1] = True
        result = 0
        
        present = collections.deque([1])
        while present:
            present_node = present.popleft()
            for next_node in connect[present_node]:
                if visit[next_node]: continue
                visit[next_node] = True
                result += 1
                present.append(next_node)
        
        print(result)

def solve2():
    for T in range(int(input())):
        N, M = map(int, input().split())
        for i in range(M): input()
        print(N - 1)
    
if "__main__" == __name__: solve2()