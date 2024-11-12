n, m = map(int, input().split())
locate = [i - 1 for i in list(map(int, input().split()))]
num_list = [i + 1 for i in range(n)]
sp_list = [num_list[i] for i in locate]
present_index, distance = 0, 0
while sp_list:
    distance += min(abs(num_list.index(sp_list[0]) - present_index), len(num_list) - max(present_index, num_list.index(sp_list[0])) + min(present_index, num_list.index(sp_list[0])))
    present_index = num_list.index(sp_list[0])
    if present_index == len(num_list) - 1: present_index = 0
    num_list.remove(sp_list[0])
    del sp_list[0]
print(distance)