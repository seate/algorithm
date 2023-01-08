import sys
input = sys.stdin.readline
IP = lambda: map(int, input().split())

def solve():
    N = (int(input()) - 1) / 3
    result = 0
    while True:
        if N <= result * (result + 1): break
        result += 1
    print(result + 1)

def other_solve():
    print(int(-(-(3+(12*int(input())-3)**.5)//6)))
    
if "__main__" == __name__: solve()