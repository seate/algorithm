import sys
input = sys.stdin.readline
IP = lambda: map(int, input().split())

def solve():
    N = int(input())
    data = [list(IP()) for i in range(N)]
    data.sort(key = lambda x: (x[1], x[0]))
    count = 0
    present_end = 0
    
    for start, end in data:
        if present_end <= start:
            count += 1
            present_end = end
    
    print(count)
    
if "__main__" == __name__: solve()