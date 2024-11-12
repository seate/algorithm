from math import gcd
import sys
input = sys.stdin.readline
IP = lambda: map(int, input().split())

def solve():
    for T in range(int(input())):
        nums = list(map(int, input().split()))
        print(nums[0] * nums[1] // gcd(*nums))
    
if "__main__" == __name__: solve()