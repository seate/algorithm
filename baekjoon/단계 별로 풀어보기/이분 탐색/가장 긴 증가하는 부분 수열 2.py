N = int(input())
A = list(map(int, input().split()))
DP = [0]

for i in range(N):
    low, high = 0, len(DP) - 1
    
    while low <= high:
        mid = (low + high) // 2
        if DP[mid] < A[i]: low = mid + 1
        else: high = mid - 1
    
    if low >= len(DP): DP.append(A[i])
    else: DP[low] = A[i]
print(len(DP) - 1)
#print(' '.join(map(str, DP[1:])))