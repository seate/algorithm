import sys
input = sys.stdin.readline

def solve():
    N, M = map(int, input().split())
    data = [0, *map(int, input().split())]
    
    for i in range(1, N): data[i + 1] += data[i]
    
    for i in range(M):
        a, b = map(int, input().split())
        print(data[b] - data[a - 1])
    
if "__main__" == __name__: solve()