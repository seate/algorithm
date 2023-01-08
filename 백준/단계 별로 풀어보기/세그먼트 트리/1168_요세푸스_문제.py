from math import log2
import sys
input = sys.stdin.readline
IP = lambda: map(int, input().split())

def solve():
    def insert(i, d, N):
        while i <= N:
            tree[i] += d
            i += (i & -i)
    
    def get(i):
        result = 0
        while i:
            result += tree[i]
            i &= (i - 1)
        return result
    
    N, K = IP()
    
    tree = [0] * (1 << int(log2(N) + 2))
    
    for i in range(1, N + 1): tree[i] = (i & -i)
    
    now = 1
    size = N
    N += 1
    print("<", end = '')
    
    while size:
        now += K - 1
        now %= size
        if not now: now += size
        
        low = 0; high = N
        while high - low != 1:
            mid = (low + high) // 2
            if now <= get(mid): high = mid
            else: low = mid
        
        if size == 1: print(high, end = ">")
        else: print(high, end = ", ")
        insert(high, -1, N)
        size -= 1
    
if "__main__" == __name__: solve()