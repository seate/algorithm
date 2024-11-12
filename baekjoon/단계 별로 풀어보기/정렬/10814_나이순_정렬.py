import sys
input = sys.stdin.readline
IP = lambda: map(int, input().split())

def solve(): print('\n'.join([' '.join(i) for i in sorted([input().split() for i in range(int(input()))], key = lambda x: int(x[0]))]))

if "__main__" == __name__: solve()