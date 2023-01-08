import sys
input = sys.stdin.readline
IP = lambda: map(int, input().split())

def solve():
    def recursion(depth = 0, present_max = 1):
        if depth == M: pr.append(' '.join(map(str, result))); return
        for i in range(present_max, N + 1):
            result[depth] = i
            recursion(depth + 1, i)
    
    N, M = IP()
    result = [None] * M
    pr = []
    recursion()
    print("\n".join(pr))
    
if "__main__" == __name__: solve()