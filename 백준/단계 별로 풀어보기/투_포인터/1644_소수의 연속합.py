from bisect import bisect_left
from itertools import accumulate
import sys
input = sys.stdin.readline
IP = lambda: map(int, input().split())

def solve():
    N = int(input())
    count, start, end, part_sum = 0, 0, 1, 2
    primes = []
    nums = [True] * (N + 1)
    
    for i in range(2, N + 1):
        if not nums[i]: continue
        primes.append(i)
        for j in range(2 * i, N + 1, i): nums[j] = False
    
    L = len(primes)
    while L:
        if N <= part_sum:
            if part_sum == N: count += 1
            part_sum -= primes[start]
            start += 1
        else:
            if L <= end: break
            part_sum += primes[end]
            end += 1
    
    print(count)

def fast():
    def prime(N):
        N += 1
        save = [True] * (N // 2)
        for i in range(3, int(N ** 0.5) + 1, 2):
            if save[i // 2]:
                k = i * i
                save[k // 2::i] = [False] * ((N - k - 1) // (2 * i) + 1)
        return [2] + [2 * i + 1 for i in range(1, N // 2) if save[i]]
    
    N = int(input())
    part_sum = [0] + list(accumulate(prime(N)))
    L = len(part_sum)
    count = 0
    start = 0
    end = bisect_left(part_sum, N) #처음 되는 곳을 이진 탐색으로 찾는다
    
    while L:
        present = part_sum[end] - part_sum[start]
        if present < N:
            end += 1
            if L == end: break
        else:
            if present == N: count += 1
            start += 1

    print(count)
    
if "__main__" == __name__:
    #solve()
    fast()