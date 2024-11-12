import math
import sys
input = sys.stdin.readline

def solve():
    N = int(input())
    parent = [[i] for i in [0, *map(int, input().split())]]
    
    for i in range(18):
        for j in range(1, N + 1): parent[j].append(parent[parent[j][i]][i])
    
    for Q in range(int(input())):
        n, x = map(int, input().split())
        logn = math.log2(n)
        ilogn = int(logn)
        while ilogn != logn:
            n -= 2 ** ilogn
            x = parent[x][ilogn]
            logn = math.log2(n)
            ilogn = int(logn)
            
        print(parent[x][ilogn])

def best_solve():#half_time
    N = int(input())
    Fk = [[0, *map(int, input().split())]]
    result = []
    
    for i in range(18):
        temp_list = Fk[-1]
        Fk.append([temp_list[temp_list[x]] for x in range(N + 1)])
    
    for Q in range(int(input())):
        n, x = map(int, input().split())
        for bit in range(19):
            if n & 1: x = Fk[bit][x]
            n >>= 1
        result.append(x)
    
    print('\n'.join(map(str, result)))

if "__main__" == __name__: best_solve()