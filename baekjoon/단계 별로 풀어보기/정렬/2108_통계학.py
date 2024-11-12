from collections import Counter
import sys
input = sys.stdin.readline
IP = lambda: map(int, input().split())

def solve():
    N = int(input())
    nums = sorted([int(input()) for i in range(N)])
    print(round(sum(nums) / N))
    print(nums[N // 2])
    
    if N == 1: print(nums[0])
    else:
        temp = Counter(nums).most_common(2)
        print(temp[1][0] if temp[0][1] == temp[1][1] else temp[0][0])
    print(nums[-1] - nums[0])
    
if "__main__" == __name__: solve()