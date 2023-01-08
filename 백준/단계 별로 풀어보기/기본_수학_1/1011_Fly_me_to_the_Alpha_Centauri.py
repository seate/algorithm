import sys
input = sys.stdin.readline
IP = lambda: map(int, input().split())

def solve():
    for T in range(int(input())):
        x, y = IP()
        sqrt = int((y - x - 1) ** 0.5)
        print(2 * sqrt + (1 if sqrt * sqrt + sqrt < y - x else 0))
    
if "__main__" == __name__: solve()