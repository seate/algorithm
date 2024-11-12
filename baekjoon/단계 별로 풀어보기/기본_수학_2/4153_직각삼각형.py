import sys
input = sys.stdin.readline
IP = lambda: map(int, input().split())

def solve():
    while True:
        a, b, c = sorted(IP())
        if not (a or b or c): break
        print("right" if a ** 2 + b ** 2 == c ** 2 else "wrong")
    
if "__main__" == __name__: solve()