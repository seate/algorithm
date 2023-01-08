from collections import defaultdict
import sys
input = sys.stdin.readline
IP = lambda: map(int, input().split())

def solve():
    for T in range(int(input())):
        kind_count = defaultdict(int)
        for i in range(int(input())): kind_count[input().split()[1]] += 1
        result = 1
        for i in kind_count.values(): result *= (i + 1)
        print(result - 1)
    
    
    
    
    
if "__main__" == __name__: solve()