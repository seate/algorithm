import sys
input = sys.stdin.readline
IP = lambda: map(int, input().split())

def solve():
    N = int(input())
    result = 0
    
    for i in range(max(1, N - 54), N):
        if N == i + sum(list(map(int, str(i)))): result = i; break
    
    print(result)
    
if "__main__" == __name__: solve()