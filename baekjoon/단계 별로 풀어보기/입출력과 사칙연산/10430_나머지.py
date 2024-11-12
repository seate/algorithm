import sys
input = sys.stdin.readline
IP = lambda: map(int, sys.stdin.readline().split())

def solve():
    a, b, c = IP()
    fir = (a + b) % c
    sec = (a * b) % c
    print(fir, fir, sec, sec, sep = '\n')
    
if "__main__" == __name__: solve()