import sys
import heapq
input = sys.stdin.readline
IP = lambda: map(int, sys.stdin.readline().split())

def solve():
    N = int(input())
    dots = []
    for _ in range(N):
        A, B = IP()
        if B < A: A, B = B, A
        heapq.heappush(dots, (A, B))
    
    answer = 0
    present_s = dots[0][0]
    present_e = dots[0][1]
    for S, E in dots[1:]:
        if S <= present_e:
            if present_e < E: present_e = E
        else:
            answer += present_e - present_s
            present_s = S
            present_e = E
    answer += present_e - present_s
    print(answer)
    
if "__main__" == __name__: solve()