import sys
input = sys.stdin.readline
IP = lambda: map(int, sys.stdin.readline().split())

def solve():
    result_index = None
    result_num = 0
    for i in range(9):
        a = int(input())
        if result_num < a:
            result_num = a
            result_index = i
    
    print(result_num)
    print(result_index + 1)
    
if "__main__" == __name__: solve()