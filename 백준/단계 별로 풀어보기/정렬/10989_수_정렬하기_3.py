import sys
input = sys.stdin.readline
IP = lambda: map(int, input().split())

def solve():
    count = [0] * (10001)
    
    for i in range(int(input())): count[int(input())] += 1
    
    for i in range(1, 10001):
        if count[i]: print(f"{i}\n" * count[i], end = "")
    
if "__main__" == __name__: solve()