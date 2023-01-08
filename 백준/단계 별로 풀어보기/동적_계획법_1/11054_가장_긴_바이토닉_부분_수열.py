from bisect import bisect_left
import sys
input = sys.stdin.readline
IP = lambda: map(int, input().split())

def solve():
    N = int(input())
    data = list(IP())
    min_list1 = [data[0]]
    min_list2 = [data[-1]]
    dp1 = []; dp2 = []; MAX = 0
    
    for present in data:
        if min_list1[-1] < present:
            min_list1.append(present)
            dp1.append(len(min_list1))
        
        else:
            index = bisect_left(min_list1, present)
            min_list1[index] = present
            dp1.append(index + 1)
    
    for present in data[::-1]:
        if min_list2[-1] < present:
            min_list2.append(present)
            dp2.append(len(min_list2))
            
        else:
            index = bisect_left(min_list2, present)
            min_list2[index] = present
            dp2.append(index + 1)
            
    
    for i, j in zip(dp1, dp2[::-1]):
        if MAX < i + j: MAX = i + j
    
    print(MAX - 1)
    
    
if "__main__" == __name__: solve()