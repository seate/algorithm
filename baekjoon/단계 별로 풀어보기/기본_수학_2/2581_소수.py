import sys
input = sys.stdin.readline
IP = lambda: map(int, input().split())

def solve():
    start = int(input()); end = int(input())
    isprime = [True] * (end + 1); primes = []
    
    for i in range(2, end + 1):
        if not isprime[i]: continue
        primes.append(i)
        for j in range(2 * i, end + 1, i): isprime[j] = False
    
    L = len(primes)
    for idx in range(L):
        if start <= primes[idx]: break
    
    if not L or primes[-1] < start: print('-1'); return
    
    print(sum(primes[idx:]))
    print(primes[idx])
    
if "__main__" == __name__: solve()