import sys
input = sys.stdin.readline
IP = lambda: map(int, sys.stdin.readline().split())

def solve():
    while True:
        try: a, b = IP()
        except: break
        print(a + b)
    
if "__main__" == __name__: solve()