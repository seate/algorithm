import sys
input = sys.stdin.readline
IP = lambda: map(int, input().split())

def solve():
    while True:
        a, b = list(map(int, input().split()))
        if not (a and b): break
        if not a % b: print("multiple")
        elif not b % a: print("factor")
        else: print("neither")
    
if "__main__" == __name__: solve()