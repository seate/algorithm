import math
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 9)
IP = lambda: map(int, sys.stdin.readline().split())
MOD = 1000000007

def segment_tree():
    def seg_init(index, start, end):
        if start == end: seg_tree[index] = data[start]
        else:
            mid = (start + end) // 2
            seg_tree[index] = (seg_init(index * 2, start, mid) * seg_init(index * 2 + 1, mid + 1, end)) % MOD
        return seg_tree[index]
    
    def get_mul(index, start, end):
        if end < b or c < start: return 1
        if b <= start and end <= c: return seg_tree[index]
        mid = (start + end) // 2
        return (get_mul(index * 2, start, mid) * get_mul(index * 2 + 1, mid + 1, end)) % MOD
    
    def update(index, start, end):
        if start != end:
            mid = (start + end) // 2
            if start <= b <= mid: update(index * 2, start, mid)
            elif mid + 1 <= b <= end: update(index * 2 + 1, mid + 1, end)
            seg_tree[index] = (seg_tree[index * 2] * seg_tree[index * 2 + 1]) % MOD
        else: seg_tree[index] = c
    
    N, M, K = map(int, input().split())
    data = [int(input()) for i in range(N)]
    seg_tree = [0] * (1 << (int(math.ceil(math.log2(N))) + 1))
    seg_init(1, 0, N - 1)
    
    for i in range(M + K):
        a, b, c = map(int, input().split())
        b -= 1
        if a == 1:
            data[b] = c
            update(1, 0, N - 1)
        else:
            c -= 1
            print(get_mul(1, 0, N - 1))

def segment_tree_other():
    N, M, K = IP()
    seg_tree = ([0] * N) + [int(input()) for i in range(N)]
    for i in range(N - 1, 0, -1): seg_tree[i] = (seg_tree[2 * i] * seg_tree[2 * i + 1]) % MOD
    
    for i in range(M + K):
        a, b, c = IP()
        b += N - 1
        if a == 1:
            seg_tree[b] = c
            while b:
                seg_tree[b // 2] = (seg_tree[b] * seg_tree[b ^ 1]) % MOD
                b //= 2
        
        else:
            c += N; result = 1
            
            while b < c:
                if b & 1:
                    result = (result * seg_tree[b]) % MOD
                    b += 1
                if c & 1: result = (result * seg_tree[c - 1]) % MOD
                b //= 2; c //= 2
            
            print(result)

if "__main__" == __name__: segment_tree_other()