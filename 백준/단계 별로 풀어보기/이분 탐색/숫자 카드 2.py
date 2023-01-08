N = int(input())
value_N = list(map(int, input().split()))
M = int(input())
value_M = list(map(int, input().split()))

checker = [0] * 20000010

for i in value_N: checker[i] += 1
for i in value_M: print(checker[i], end = ' ')