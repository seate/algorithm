from itertools import combinations
import sys
input = sys.stdin.readline
IP = lambda: map(int, input().split())

def solve():
    N, max_weight = IP()
    weights = [i for i in IP() if i <= max_weight]; N = len(weights)
    group1 = []; group2 = []; half = N // 2
    
    for i in range(1, half + 1):
        for weight_sum in map(sum, combinations(weights[:half], i)):
            if weight_sum <= max_weight: group1.append(weight_sum)
        for weight_sum in map(sum, combinations(weights[half:], i)):
            if weight_sum <= max_weight: group2.append(weight_sum)
    if N & 1: #N이 홀수면 right의 전체를 더한 값을 더 추가해야함
        S = sum(weights[half:])
        if S <= max_weight: group2.append(S)
    
    group1.sort()
    group2.sort()
    
    group1_length = len(group1)
    start = 0; end = len(group2) - 1
    count = group1_length + end + 2 #group 각각 개수 + 아무것도 넣지 않는 것 1
    
    while group1 and group2:
        if group1[start] + group2[end] <= max_weight:
            count += end + 1
            start += 1
            if group1_length <= start: break
        
        else:
            end -= 1
            if end < 0: break
    
    print(count)
    
if "__main__" == __name__: solve()