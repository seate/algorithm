import sys
input = sys.stdin.readline
IP = lambda: map(int, input().split())

def solve():
    N, rest = IP()
    unit = [int(input()) for i in range(N)]
    count = 0
    
    for present_unit in unit[::-1]:
        if rest < present_unit: continue
        count += rest // present_unit
        rest %= present_unit
    
    print(count)
    
if "__main__" == __name__: solve()