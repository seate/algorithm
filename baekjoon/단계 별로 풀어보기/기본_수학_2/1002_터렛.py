import sys
input = sys.stdin.readline
IP = lambda: map(int, input().split())

def solve():
    for T in range(int(input())):
        x1, y1, r1, x2, y2, r2 = IP()
        center_distance = (abs(x2 - x1) ** 2 + abs(y2 - y1) ** 2) ** 0.5
        if x1 == x2 and y1 == y2 and r1 == r2: print('-1')
        elif r1 + r2 < center_distance: print('0')
        elif r1 + r2 == center_distance: print('1')
        elif abs(r1 - r2) < center_distance < (r1 + r2): print('2')
        elif abs(r1 - r2) == center_distance: print('1')
        elif center_distance < abs(r1 - r2): print('0')
    
if "__main__" == __name__: solve()