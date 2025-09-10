M = 0
v = [list(map(int, input().split())) for _ in range(9)]

for y in range(9):
    for x in range(9):
        if M <= v[y][x]:
            M = v[y][x]
            Y, X = y, x

print(M)
print(Y + 1, X + 1)