import sys
input = sys.stdin.readline
IP = lambda: map(int, input().split())

def solve():
    N, MAX = IP()
    nums = list(IP())
    result = 0
    
    for i in range(N - 2):
        for j in range(i + 1, N - 1):
            for k in range(j + 1, N):
                present = nums[i] + nums[j] + nums[k]
                if present == MAX: result = MAX; break
                elif result < present < MAX: result = present
    
    print(result)
    
if "__main__" == __name__: solve()