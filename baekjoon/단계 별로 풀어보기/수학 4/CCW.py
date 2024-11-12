import sys
input = sys.stdin.readline

def solve():
    def get_incline(d1, d2): return "inf" if d1[0] == d2[0] else (d2[1] - d1[1]) / (d2[0] - d1[0])
    
    dot = [tuple(map(int, input().split())) for i in range(3)]
    incline1 = get_incline(dot[0], dot[1])
    
    if incline1 == get_incline(dot[1], dot[2]): print(0)
    else: print(1 if bool(dot[0][0] < dot[1][0]) == bool((dot[2][0] - dot[0][0]) * incline1 < dot[2][1] - dot[0][1]) else -1)

def fastest_solve():
    dot = [list(map(int, sys.stdin.readline().split())) for i in range(3)]
    judge = (dot[1][0] - dot[0][0]) * (dot[2][1] - dot[1][1]) - (dot[1][1] - dot[0][1]) * (dot[2][0] - dot[1][0])
    print((judge > 0) - (judge < 0))

if "__main__" == __name__: fastest_solve()