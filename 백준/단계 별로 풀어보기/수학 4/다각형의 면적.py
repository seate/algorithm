import sys
input = sys.stdin.readline

def solve():
    N = int(input())
    dot = [tuple(map(int, input().split())) for i in range(N)]; dot.append(dot[0])
    result = 0
    for i in range(N): result += (dot[i][0] * dot[i + 1][1]) - (dot[i][1] * dot[i + 1][0])
    print(round(abs(result) / 2, 1))
    
if "__main__" == __name__: solve()