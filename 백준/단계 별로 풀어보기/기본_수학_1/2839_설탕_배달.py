import sys

def solve():
    N = int(sys.stdin.readline())
    count = N // 5
    remain = N % 5
    
    while count and remain % 3:
        count -= 1
        remain += 5
    
    print("-1" if remain % 3 else count + (remain // 3))
    
if "__main__" == __name__: solve()