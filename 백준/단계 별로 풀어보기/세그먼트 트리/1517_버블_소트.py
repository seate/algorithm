import sys
input = sys.stdin.readline
IP = lambda: map(int, input().split())

def solve():
    def dfs(start, end):
        if start == end: return [initial_list[start]]
        elif end == start + 1:
            if initial_list[start] <= initial_list[end]: return [initial_list[start], initial_list[end]]
            else:
                counter[0] += 1
                return [initial_list[end], initial_list[start]]
        
        mid = (start + end) // 2
        L1 = dfs(start, mid)
        L2 = dfs(mid + 1, end)
        
        L1_length = mid - start + 1
        L2_length = end - mid
        idx1 = 0; idx2 = 0
        part_result = []
        
        while idx1 < L1_length and idx2 < L2_length:
            if L1[idx1] <= L2[idx2]:
                part_result.append(L1[idx1])
                idx1 += 1
            else:
                counter[0] += L1_length - idx1
                part_result.append(L2[idx2])
                idx2 += 1
        
        part_result += L1[idx1:]
        part_result += L2[idx2:]
        
        return part_result
    
    length = int(input())
    initial_list = list(IP())
    counter = [0]
    dfs(0, length - 1)
    print(counter[0])
    
if "__main__" == __name__: solve()