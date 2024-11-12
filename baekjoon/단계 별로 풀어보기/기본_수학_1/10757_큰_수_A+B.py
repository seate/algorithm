import sys
input = sys.stdin.readline
IP = lambda: map(int, input().split())

def solve(): print(sum(IP()))
    
if "__main__" == __name__: solve()