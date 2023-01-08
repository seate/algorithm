import sys
input = sys.stdin.readline
IP = lambda: map(int, input().split())

def solve():
    input(); count = 0
    for d in list(IP()):
        isit = True
        if d == 1: isit = False
        for i in range(2, int(d ** 0.5) + 1):
            if not d % i: isit = False; break
        count += isit
    print(count)
    
if "__main__" == __name__: solve()