from collections import deque
import sys
input = sys.stdin.readline
IP = lambda: map(int, input().split())

def solve():
    N, K = IP()
    K -= 1
    L = deque(range(1, N + 1))
    result = []
    
    while L:
        L.rotate(-K)
        result.append(L.popleft())
    
    print("<", ", ".join(map(str, result)), ">", sep = "")
    
if "__main__" == __name__: solve()