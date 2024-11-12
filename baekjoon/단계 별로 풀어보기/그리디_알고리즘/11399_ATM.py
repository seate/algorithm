import sys
input = sys.stdin.readline
IP = lambda: map(int, input().split())

def solve():
    N = int(input())
    print(sum(list(map(lambda iv: iv[1] * (N - iv[0]), enumerate(sorted(IP()))))))
    
if "__main__" == __name__: solve()