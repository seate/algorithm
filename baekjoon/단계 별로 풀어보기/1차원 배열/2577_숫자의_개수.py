import sys
input = sys.stdin.readline
IP = lambda: map(int, sys.stdin.readline().split())

def solve():
    counter = [0] * 10
    for num in str(int(input()) * int(input()) * int(input())): counter[int(num)] += 1
    print('\n'.join(map(str, counter)))
    
if "__main__" == __name__: solve()