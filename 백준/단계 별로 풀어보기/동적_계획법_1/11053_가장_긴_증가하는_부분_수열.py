from bisect import bisect_left
import sys
input = sys.stdin.readline
IP = lambda: map(int, input().split())

def solve():
    N = int(input())
    data = list(IP())
    min_list = [data[0]]
    
    for present in data:
        if min_list[-1] < present: min_list.append(present)
        else: min_list[bisect_left(min_list, present)] = present
    
    print(len(min_list))

if "__main__" == __name__: solve()