from itertools import product
import sys
input = sys.stdin.readline
IP = lambda: map(int, input().split())

def solve():
    N, M = IP()
    print('\n'.join([' '.join(map(str, i)) for i in product(list(range(1, N + 1)), repeat = M)]))
    
if "__main__" == __name__: solve()