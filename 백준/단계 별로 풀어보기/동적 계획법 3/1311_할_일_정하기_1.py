from collections import deque
import sys
input = sys.stdin.readline
IP = lambda: map(int, input().split())
INF = float("inf")

def solve():
    N = int(input())
    data = [list(IP()) for i in range(N)]
    
    fac = [1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880, 3628800, 39916800, 479001600, 6227020800, 87178291200, 1307674368000, 20922789888000, 355687428096000, 6402373705728000, 121645100408832000, 2432902008176640000]
    next_locate = deque([(1 << i) for i in range(N)])
    dp = [INF] * (1 << N)
    for i in range(N): dp[1 << i] = data[0][i]
    
    for y in range(1, N):
        L = fac[N] // (fac[y] * fac[N - y])
        while L:
            nxt = next_locate.popleft()
            for i in range(N):
                if not ((1 << i) & nxt):
                    nl = nxt | (1 << i)
                    if dp[nl] == INF: next_locate.append(nl)
                    if dp[nxt] + data[y][i] < dp[nl]: dp[nl] = dp[nxt] + data[y][i]
            L -= 1
    
    print(dp[-1])

def hungarian_algorithm(): pass
    
if "__main__" == __name__: solve()