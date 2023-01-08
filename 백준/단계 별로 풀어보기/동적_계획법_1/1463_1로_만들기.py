from collections import deque
import sys
input = sys.stdin.readline
IP = lambda: map(int, input().split())

def solve():
    N = int(input())
    if N == 1: print("0"); return
    dp = [0] * (N + 1)
    
    que = deque([N])
    while not dp[1]:
        present = que.popleft()
        
        if not present % 3 and not dp[present // 3]:
            dp[present // 3] = dp[present] + 1
            que.append(present // 3)
        if not present & 1 and not dp[present // 2]:
            dp[present // 2] = dp[present] + 1
            que.append(present // 2)
        
        if not dp[present - 1]:
            dp[present - 1] = dp[present] + 1
            que.append(present - 1)
    
    print(dp[1])
    
if "__main__" == __name__: solve()