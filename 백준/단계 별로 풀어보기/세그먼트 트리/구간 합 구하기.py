import math
import sys
input = sys.stdin.readline
IP = lambda: map(int, sys.stdin.readline().split())
sys.setrecursionlimit(10 ** 9)

def segment_tree():
    def seg_init(index, start, end):
        if start == end: seg_tree[index] = data[start]
        else:
            mid = (start + end) // 2
            seg_tree[index] = seg_init(index * 2, start, mid) + seg_init(index * 2 + 1, mid + 1, end)
        return seg_tree[index]
    
    
    def get_sum(index, start, end):
        if end < b or c < start: return 0
        if b <= start and end <= c: return seg_tree[index]
        mid = (start + end) // 2
        return get_sum(index * 2, start, mid) + get_sum(index * 2 + 1, mid + 1, end)
    
    
    def update(index, start, end):
        if not start <= b <= end: return
        seg_tree[index] += differ
        if start == end: return
        mid = (start + end) // 2
        if start <= b <= mid: update(index * 2, start, mid)
        if mid + 1 <= b <= end: update(index * 2 + 1, mid + 1, end)
    
    N, M, K = IP()
    data = [int(input()) for i in range(N)]
    seg_tree = [0] * (1 << (int(math.ceil(math.log2(N))) + 1))
    
    seg_init(1, 0, N - 1)
    
    for i in range(M + K):
        a, b, c = IP()
        b -= 1
        if a == 1:
            differ = c - data[b]
            data[b] = c
            update(1, 0, N - 1)
        else:
            c -= 1
            print(get_sum(1, 0, N - 1))


def segment_tree_other():
    N, M, K = IP()
    seg_tree = ([0] * N) + [int(input()) for i in range(N)]
    for i in range(N - 1, 0, -1): seg_tree[i] = seg_tree[2 * i] + seg_tree[2 * i + 1]
    
    for i in range(M + K):
        a, b, c = IP()
        b += N - 1
        if a == 1:
            seg_tree[b] = c
            while b:
                seg_tree[b // 2] = seg_tree[b] + seg_tree[b ^ 1]
                b //= 2
        else:
            c += N; result = 0
            
            while b < c:
                if b & 1:
                    result += seg_tree[b]
                    b += 1
                
                if c & 1:
                    c -= 1
                    result += seg_tree[c]
                
                b //= 2; c //= 2
            
            print(result)

def Fenwick_tree_my_solve():
    N, M, K = IP()
    data = [0] + [int(input()) for i in range(N)]
    fenwick_tree = [0] * (N + 1)
    
    for i in range(1, N + 1):
        plus = data[i]
        while i <= N:
            fenwick_tree[i] += plus
            i += (i & -i)
    
    for i in range(M + K):
        a, b, c = map(int, input().split())
        if a == 1:
            differ = c - data[b]
            data[b] = c
            while b <= N:
                fenwick_tree[b] += differ
                b += (b & -b)
        
        else:
            result = 0; b -= 1
            
            while 0 < c:
                result += fenwick_tree[c]
                c -= (c & -c)
            
            while 0 < b:
                result -= fenwick_tree[b]
                b -= (b & -b)
            
            print(result)

    
if "__main__" == __name__:
    #segment_tree()
    #segment_tree_other()
    Fenwick_tree_my_solve()