import sys
input = sys.stdin.readline
IP = lambda: map(int, input().split())

def solve():
    N, S = IP()
    data = list(IP())
    part_sum, result_length = data[0], N + 1
    start, end = 0, 1
    
    while True:
        if S <= part_sum:
            if end - start < result_length: result_length = end - start
            part_sum -= data[start]
            start += 1
        else:
            if N <= end: break
            part_sum += data[end]
            end += 1
    
    print(result_length % (N + 1))
    
if "__main__" == __name__: solve()