import sys
input = sys.stdin.readline
IP = lambda: map(int, input().split())

def solve():
    def counter(n, div):
        count = 0
        while n:
            n //= div
            count += n
        return count
    
    N, M = IP()
    print(min(counter(N, 5) - counter(M, 5) - counter(N - M, 5), counter(N, 2) - counter(M, 2) - counter(N - M, 2)))
    
if "__main__" == __name__: solve()