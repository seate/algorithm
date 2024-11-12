import sys
input = sys.stdin.readline
IP = lambda: map(int, input().split())

def solve():
    N = int(input())
    data = list(IP())
    dp = [data[0]]
    for i in range(1, N): dp += [data[i] if dp[-1] <= 0 else dp[-1] + data[i]]
    
    print(max(dp))

if "__main__" == __name__: solve()