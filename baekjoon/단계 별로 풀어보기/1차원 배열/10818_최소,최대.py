import sys
input = sys.stdin.readline
IP = lambda: map(int, sys.stdin.readline().split())

def solve():
    m = float("inf"); M = -float("inf"); input()
    for each in IP():
        if each < m: m = each
        if M < each: M = each
    print(m, M)
    
if "__main__" == __name__: solve()