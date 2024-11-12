import sys
input = sys.stdin.readline
IP = lambda: map(int, sys.stdin.readline().split())

def solve():
    a, b = IP()
    print(a + b, a - b, a * b, a // b, a % b, sep = '\n')
    
if "__main__" == __name__: solve()