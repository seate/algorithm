import sys
input = sys.stdin.readline
IP = lambda: map(int, sys.stdin.readline().split())

def solve():
    a = int(input())
    if 90 <= a: print("A")
    elif 80 <= a: print("B")
    elif 70 <= a: print("C")
    elif 60 <= a: print("D")
    else: print("F")
    
if "__main__" == __name__: solve()