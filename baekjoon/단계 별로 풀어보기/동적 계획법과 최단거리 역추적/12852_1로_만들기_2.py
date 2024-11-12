from collections import deque
import sys
input = sys.stdin.readline
IP = lambda: map(int, input().split())

def solve():
    N = int(input())
    visited = [False] * (N + 1); visited[N] = True
    
    q = deque([N])
    while True:
        present = q.popleft()
        fir = present // 3
        sec = present // 2
        thi = present - 1
        if not present % 3 and not visited[fir]:
            visited[fir] = present
            q.append(fir)
        if not present & 1 and not visited[sec]:
            visited[sec] = present
            q.append(sec)
        if 0 < thi and not visited[thi]:
            visited[thi] = present
            q.append(thi)
        if visited[1]: break
    
    trace = [1]; present = 1
    while present != N:
        present = visited[present]
        trace.append(present)
    print(len(trace) - 1)
    print(' '.join(map(str, trace[::-1])))


def fast_solve():
    save = {1:0, 2:1}
    def dfs(present):
        if present in save: return save[present]
        a = dfs(present // 2) + 1 + present % 2
        b = dfs(present // 3) + 1 + present % 3
        save[present] = a if a < b else b
        return save[present]
    
    N = int(input())
    print(dfs(N))
    result = [N]
    
    while 1 < N:
        if save[N] == save[N // 2] + 1 + N % 2:
            if N & 1: result.append(N - 1)
            N //= 2
            result.append(N)
        else:
            while N % 3:
                N -= 1
                result.append(N)
            N //= 3
            result.append(N)
    
    print(' '.join(map(str, result)))

if "__main__" == __name__:
    #solve()
    fast_solve()