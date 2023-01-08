import sys
input = sys.stdin.readline
IP = lambda: map(int, input().split())

def solve():
    N = int(input())
    data = [list(IP()) for i in range(N)]
    
    for y in range(1, N):
        data[y][0] += data[y - 1][0]
        for x in range(1, y): data[y][x] += (data[y - 1][x] if data[y - 1][x - 1] < data[y - 1][x] else data[y - 1][x - 1])
        data[y][-1] += data[y - 1][-1]
    
    print(max(data[-1]))
    
if "__main__" == __name__: solve()