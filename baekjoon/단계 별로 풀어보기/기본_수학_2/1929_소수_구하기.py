import sys
input = sys.stdin.readline
IP = lambda: map(int, input().split())

def solve():
    start, end = IP()
    end += 1
    save = [True] * (end // 2)
    for i in range(3, int(end ** 0.5) + 1, 2):
        if save[i // 2]:
            k = i * i
            save[k // 2 :: i] = [False] * ((end - k - 1) // (2 * i) + 1)
    primes = [2] + [2 * i + 1 for i in range(1, end // 2) if save[i]]
    
    for idx in range(len(primes)):
        if start <= primes[idx]: break
    
    print('\n'.join(map(str, primes[idx:])))
    
if "__main__" == __name__: solve()