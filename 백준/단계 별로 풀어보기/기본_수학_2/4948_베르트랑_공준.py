from bisect import bisect_left, bisect_right
import sys
input = sys.stdin.readline
IP = lambda: map(int, input().split())

def solve():
    Ns = []
    while True:
        scaned = int(input())
        if not scaned: break
        Ns.append(scaned)
    
    end = max(Ns) * 2 + 1
    save = [True] * (end // 2)
    for i in range(3, int(end ** 0.5) + 1, 2):
        if save[i // 2]:
            k = i * i
            save[k // 2 :: i] = [False] * ((end - k - 1) // (2 * i) + 1)
    primes = [2] + [2 * i + 1 for i in range(1, end // 2) if save[i]]
    
    print('\n'.join(map(str, [bisect_right(primes, 2 * n) - bisect_left(primes, n + 1) for n in Ns])))
    
if "__main__" == __name__: solve()