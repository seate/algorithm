import math
import sys
input = sys.stdin.readline
IP = lambda: map(int, sys.stdin.readline().split())

def solve():
    def seg_init(index, start, end):
        if start == end: seg_tree[index] = [data[start], data[end]]
        else:
            mid = (start + end) // 2
            A = seg_init(index * 2, start, mid); B = seg_init(index * 2 + 1, mid + 1, end)
            seg_tree[index] = [A[0] if A[0] < B[0] else B[0], A[1] if B[1] < A[1] else B[1]]
        return seg_tree[index]
    
    def get_Mm(index, start, end):
        if end < a or b < start: return False
        if a <= start and end <= b: return seg_tree[index]
        mid = (start + end) // 2
        A = get_Mm(index * 2, start, mid); B = get_Mm(index * 2 + 1, mid + 1, end)
        
        if A and B: return [A[0] if A[0] < B[0] else B[0], A[1] if B[1] < A[1] else B[1]]
        elif A: return A
        elif B: return B
    
    N, M = IP()
    data = [int(input()) for i in range(N)]
    seg_tree = [0] * (1 << (int(math.ceil(math.log2(N))) + 1))
    seg_init(1, 0, N - 1)
    for i in range(M):
        a, b = IP()
        a -= 1; b -= 1
        print(*get_Mm(1, 0, N - 1))

def segment_tree_other():
    N, Q = IP()
    original_data = [int(input()) for _ in range(N)]
    seg_m = ([0] * N) + original_data[:]
    seg_M = seg_m[:]
    
    for i in range(N - 1, 0, -1):
        seg_m[i] = seg_m[2 * i] if seg_m[2 * i] < seg_m[2 * i + 1] else seg_m[2 * i + 1]
        seg_M[i] = seg_M[2 * i] if seg_M[2 * i + 1] < seg_M[2 * i] else seg_M[2 * i + 1]
    
    for i in range(Q):
        a, b = IP()
        a += N - 1; b += N
        result_m = float("inf")
        result_M = 0
        
        while a < b:
            if a & 1:
                if seg_m[a] < result_m: result_m = seg_m[a]
                if result_M < seg_M[a]: result_M = seg_M[a]
                a += 1
            
            if b & 1:
                b -= 1
                if seg_m[b] < result_m: result_m = seg_m[b]
                if result_M < seg_M[b]: result_M = seg_M[b]
            
            a //= 2; b //= 2
        
        print(result_m, result_M)
    
if "__main__" == __name__:
    #solve()
    segment_tree_other()