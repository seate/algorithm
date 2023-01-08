import sys
input = sys.stdin.readline
IP = lambda: map(int, input().split())

def solve():
    N = int(input())
    present = 666
    while N:
        if "666" in str(present): N -= 1
        present += 1
    print(present - 1)
    
if "__main__" == __name__: solve()