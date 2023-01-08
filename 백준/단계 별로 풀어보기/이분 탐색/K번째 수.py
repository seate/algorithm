N, K = int(input()), int(input())
start, end = 1, K
while start <= end:
    mid, temp = (start + end) // 2, 0
    for i in range(1, N + 1): temp += min(mid // i, N)
    if temp >= K: answer, end = mid, mid - 1
    else: start = mid + 1
print(answer)