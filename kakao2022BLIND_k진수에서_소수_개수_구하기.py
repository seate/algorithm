from math import sqrt

def conv(n, k):
    result = []
    while n != 0:
        rem = n % k
        result.append(str(rem))
        n = n // k
    
    return reversed(result)
    
def getnums(nums):
    return list(map(int, filter(None, ''.join(nums).split("0"))))


PrimeCache = {1: False, 2: True}
def isPrime(n):
    if n in PrimeCache: return PrimeCache[n]
    
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            PrimeCache[n] = False
            return False
    
    PrimeCache[n] = True
    return True


def solution(n, k):
    return sum(1 for a in getnums(conv(n, k)) if isPrime(a))