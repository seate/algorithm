from collections import deque
import sys
input = sys.stdin.readline
IP = lambda: map(int, input().split())

def module():
    d = deque(range(int(input())))
    while len(d) != 1:
        d.popleft()
        d.rotate(-1)
    print(d[0] + 1)
    
def slicing():
    start = 1
    L = list(range(int(input())))
    while len(L) != 1:
        if len(L) & 1:
            L = L[start::2]
            start ^= 1
        else: L = L[start::2]
    print(L[0] + 1)

def fastest():
    def cal(n):
        i = 1
        while i < n: i <<= 1
        if i != n or not N & 1: i >>= 1
        return i
    
    N = int(input())
    if N <= 2: print(N); return
    print(4 * (N // 2 - cal(N // 2)) + 2 * (N & 1))
    
if "__main__" == __name__:
    #module()
    #slicing()
    fastest()