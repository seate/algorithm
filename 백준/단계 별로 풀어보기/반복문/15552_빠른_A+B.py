import sys
input = sys.stdin.readline
IP = lambda: map(int, sys.stdin.readline().split())

def solve():
    result = []
    for T in range(int(input())):
        a, b = IP()
        result.append(a + b)
    
    print('\n'.join(map(str, result)))
    
if "__main__" == __name__: solve()