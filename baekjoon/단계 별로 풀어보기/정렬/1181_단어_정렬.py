import sys
input = sys.stdin.readline
IP = lambda: map(int, input().split())

def solve(): print('\n'.join(sorted(sorted({input().rstrip() for i in range(int(input()))}), key = len)))
    
if "__main__" == __name__: solve()