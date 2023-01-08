from sys import stdin

def solve():
    N, M = map(int, stdin.readline().split())
    count = 0
    str_set = {stdin.readline() for i in range(N)}
    
    for i in range(M):
        if stdin.readline() in str_set: count += 1
    
    print(count)

if "__main__" == __name__: solve()