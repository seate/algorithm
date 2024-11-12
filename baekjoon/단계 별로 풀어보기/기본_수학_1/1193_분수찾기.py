import sys
input = sys.stdin.readline
IP = lambda: map(int, input().split())

def solve():
    N = int(input()) * 2
    s = 1
    while True:
        if N <= s * (s + 1): break;
        s += 1
    
    y = (N - s * (s - 1)) // 2
    
    print(str(s - y + 1) + '/' + str(y) if s & 1 else str(y) + '/' + str(s - y + 1))
    
if "__main__" == __name__: solve()