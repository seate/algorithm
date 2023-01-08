import sys
input = sys.stdin.readline

def solve():
    def CCW(a, b, c):
        judge = (b[0] - a[0]) * (c[1] - b[1]) - (b[1] - a[1]) * (c[0] - b[0])
        return (judge > 0) - (judge < 0)
    
    x1, y1, x2, y2 = map(int, input().split())
    x3, y3, x4, y4 = map(int, input().split())
    
    A = (x1, y1); B = (x2, y2); C = (x3, y3); D = (x4, y4)
    j1 = CCW(A, B, C) * CCW(A, B, D); j2 = CCW(C, D, A) * CCW(C, D, B)
    if j1 == j2 == 0:
        if A[0] == C[0]:
            if y2 < y1: A, B = B, A
            if y4 < y3: C, D = D, C
            print(int(A[1] <= D[1] and C[1] <= B[1]))
        
        else:
            if x2 < x1: A, B = B, A
            if x4 < x3: C, D = D, C
            print(int(A[0] <= D[0] and C[0] <= B[0]))
    
    else: print(int(j1 <= 0 and j2 <= 0))
    
if "__main__" == __name__: solve()