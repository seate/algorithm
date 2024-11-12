import sys
input = sys.stdin.readline
IP = lambda: map(int, sys.stdin.readline().split())

def solve():
    a, b = IP()
    if a > b: print(">")
    elif a == b: print("==")
    else: print("<")
    
if "__main__" == __name__: solve()