def router_counter(distance):
    count = 1
    cur_house = house[0]
    for i in range(1, N):
        if cur_house + distance <= house[i]:
            count += 1
            cur_house = house[i]
    return count

N, C = map(int, input().split())
house = sorted([int(input()) for i in range(N)])
start, end = 1, house[-1] - house[0]

while start <= end:
    mid = (start + end) // 2
    if router_counter(mid) >= C: answer, start = mid, mid + 1
    else: end = mid - 1
print(answer)