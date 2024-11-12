import sys
input = sys.stdin.readline
IP = lambda: map(int, input().split())

def solve():
    N = int(input())
    nums = set(IP())
    x = int(input())
    count = 0
    
    for num in nums:
        if x - num in nums: count += 1
    
    print(count // 2)

def two_pointer():
    start, end, count = 0, int(input()) - 1, 0
    data = sorted(IP())
    X = int(input())
    
    while start < end:
        present = data[start] + data[end]
        if present <= X:
            if present == X: count += 1
            start += 1
        else: end -= 1
    
    print(count)

if "__main__" == __name__:
    #solve()
    two_pointer()