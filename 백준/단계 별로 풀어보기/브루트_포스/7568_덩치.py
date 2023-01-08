import sys
input = sys.stdin.readline
IP = lambda: map(int, input().split())

def solve():
    N = int(input())
    result = [1] * N
    l = []
    
    for i in range(N): l.append(tuple(IP()))
    
    for present in range(N):
        temp = 1
        for n in range(N):
            if l[present][0] < l[n][0] and l[present][1] < l[n][1]: temp += 1
        result[present] = temp
    
    print(' '.join(map(str, result)))
    
if "__main__" == __name__: solve()