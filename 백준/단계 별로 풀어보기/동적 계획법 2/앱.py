import sys
input = sys.stdin.readline

N, M = map(int, input().split())
apps, all_cost, cost_to_present_sum, last, minimum = [], 0, 0, 0, float("inf")
for i in list(zip(map(int, input().split()), map(int, input().split()))): apps.append(i)
for i in range(2): apps.sort(key = lambda x: x[i])
for i in apps: all_cost += i[1]
dp = [0 for j in range(all_cost + 1)]


for i in range(N):
    #계산해야 하는 부분
    cost_to_present_sum += apps[i][1]
    for j in range(cost_to_present_sum, apps[i][1] - 1, -1):
        dp[j] = max(dp[j], dp[j - apps[i][1]] + apps[i][0])
        if M <= dp[j]: minimum = min(minimum, j)
    dp[cost_to_present_sum + 1:] = [dp[cost_to_present_sum]] * (all_cost - cost_to_present_sum)
print(minimum)