import sys
input = sys.stdin.readline

def solve():
    def CCW(a, b, c):
        judge = (b[0] - a[0]) * (c[1] - b[1]) - (b[1] - a[1]) * (c[0] - b[0])
        return (judge > 0) - (judge < 0)
    
    x1, y1, x2, y2 = map(int, input().split())
    x3, y3, x4, y4 = map(int, input().split())
    A = (x1, y1); B = (x2, y2); C = (x3, y3); D = (x4, y4)
    
    print(int(CCW(A, B, C) * CCW(A, B, D) <= 0 and CCW(C, D, A) * CCW(C, D, B) <= 0))
    
if "__main__" == __name__: solve()