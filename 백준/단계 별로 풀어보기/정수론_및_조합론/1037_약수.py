import sys
input = sys.stdin.readline
IP = lambda: map(int, input().split())

def solve():
    input()
    data = sorted(IP())
    print(data[0] * data[-1])

if "__main__" == __name__: solve()