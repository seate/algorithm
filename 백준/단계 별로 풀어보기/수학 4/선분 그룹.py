import sys
input = sys.stdin.readline
IP = lambda: map(int, sys.stdin.readline().split())

def solve():
    def find_parent(search):
        if parent[search] < 0: return search
        parent[search] = find_parent(parent[search])
        return parent[search]
    
    def CCW(a, b, c):
        judge = (b[0] - a[0]) * (c[1] - b[1]) - (b[1] - a[1]) * (c[0] - b[0])
        return (judge > 0) - (judge < 0)
    
    def line_cross(l1, l2):
        A, B = l1; C, D = l2
        j1 = CCW(A, B, C) * CCW(A, B, D); j2 = CCW(C, D, A) * CCW(C, D, B)
        if j1 == j2 == 0:
            if A[0] == C[0]:
                if B[1] < A[1]: A, B = B, A
                if D[1] < C[1]: C, D = D, C
                return (A[1] <= D[1] and C[1] <= B[1])
            else:
                if B[0] < A[0]: A, B = B, A
                if D[0] < C[0]: C, D = D, C
                return (A[0] <= D[0] and C[0] <= B[0])
        else: return (j1 <= 0 and j2 <= 0)
    
    N = int(input())
    lines, parent, MAX, group = [], [-1] * N, 0, 0
    for i in range(N):
        x1, y1, x2, y2 = IP()
        if x2 < x1: x1, x2, y1, y2 = x2, x1, y2, y1
        lines.append(((x1, y1), (x2, y2)))
    lines.sort()
    
    for fir in range(N - 1):
        for sec in range(fir + 1, N):
            if lines[fir][1][0] < lines[sec][0][0]: break
            if line_cross(lines[fir], lines[sec]):
                F = find_parent(fir); S = find_parent(sec)
                if F == S: continue
                elif parent[F] > parent[S]: parent[F] += parent[S]; parent[S] = F
                else: parent[S] += parent[F]; parent[F] = S
    
    for i in range(N):
        if parent[i] < 0:
            group += 1
            if parent[i] < MAX: MAX = parent[i]
    
    print(group)
    print(-MAX)
    
if "__main__" == __name__: solve()