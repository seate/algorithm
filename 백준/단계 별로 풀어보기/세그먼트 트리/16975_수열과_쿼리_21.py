import sys
import math
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 9)
IP = lambda: map(int, sys.stdin.readline().split())

def lazy_propaganda():
    def tree_init(index, start, end):
        if start == end: segment_tree[index] = data[start]
        else:
            mid = (start + end) // 2
            tree_init(index * 2, start, mid)
            tree_init(index * 2 + 1, mid + 1, end)
    
    def update(index, start, end):
        if plus_start <= start and end <= plus_end: lazy[index] += plus
        else:
            mid = (start + end) // 2
            if plus_start <= mid: update(index * 2, start, mid)
            if mid + 1 <= plus_end : update(index * 2 + 1, mid + 1, end)
    
    def get_value():
        index = 1; result = lazy[1]
        start = 0; end = N - 1
        
        while start != end:
            mid = (start + end) // 2
            index <<= 1
            if destination <= mid: end = mid
            else:
                start = mid + 1
                index += 1
            result += lazy[index]
        print(result + data[destination])
    
    
    N = int(input())
    data = list(IP())
    segment_tree = [0] * (1 << int(math.log2(N) + 2))
    lazy = [0] * (1 << int(math.log2(N) + 2))
    
    tree_init(1, 0, N - 1)
    
    for i in range(int(input())):
        query = list(IP())
        if query[0] == 1:
            plus_start, plus_end, plus = query[1] - 1, query[2] - 1, query[3]
            update(1, 0, N - 1)
        else:
            destination = query[1] - 1
            get_value()
    

def other_solve():
    def update(left, right, plus):
        while left <= right:
            if left & 1:
                tree[left] += plus
                left += 1
            if not right & 1:
                tree[right] += plus
                right -= 1
            
            left //= 2
            right //= 2
    
    def get_value(left):
        count = 0
        while 1 <= left:
            count += tree[left]
            left //= 2
        return count
    
    N = int(input())
    tree = [0] * N + list(IP())
    
    for i in range(int(input())):
        query = list(IP())
        if query[0] == 1: update(query[1] + N - 1, query[2] + N - 1, query[3]) #update와 propaganda를 겸해서 행한다. 
        else: print(get_value(query[1] + N - 1))

if "__main__" == __name__:
    #lazy_propaganda()
    other_solve()