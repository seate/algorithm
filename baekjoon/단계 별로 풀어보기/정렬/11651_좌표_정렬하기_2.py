import sys
input = sys.stdin.readline
IP = lambda: map(int, input().split())

def solve():
    for each in sorted([tuple(IP()) for i in range(int(input()))], key = lambda x: (x[1], x[0])): print(*each)
    
if "__main__" == __name__: solve()