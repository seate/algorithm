from itertools import permutations
import sys
input = sys.stdin.readline
IP = lambda: map(int, input().split())

def solve():
    N, M = IP()
    print('\n'.join([' '.join(map(str, i)) for i in permutations(list(range(1, N + 1)), M)]))
    
if "__main__" == __name__: solve()