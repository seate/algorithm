import sys
input = sys.stdin.readline
IP = lambda: map(int, input().split())

def solve():
    N = 1 << 21
    seg = [0] * (2 * N)
    result = []
    for i in range(int(input())):
        choise, k = IP()
        if choise == 1:
            pos = k + N - 1
            while pos:
                seg[pos] += 1
                pos >>= 1
            
        else:
            pos = 1
            while pos < N:
                pos <<= 1
                if seg[pos] < k: k -= seg[pos]; pos += 1
            
            result.append(pos - N + 1)
            
            while pos:
                seg[pos] -= 1
                pos >>= 1
    
    print('\n'.join(map(str, result)))

if "__main__" == __name__: solve()