def square(first_matrix, second_matrix, c):
    result_matrix = [[0 for j in range(N)] for i in range(N)]
    for i in range(N):
        for j in range(N):
            for k in range(N): result_matrix[i][j] += (first_matrix[i][k] * second_matrix[k][j]) % c
    return [[j % c for j in i] for i in result_matrix]

def exponent(a, b, c):
    if b == 1: return [[j % c for j in i] for i in original_matrix]
    elif b % 2 == 1: return square(exponent(a, b - 1, c), original_matrix, c)
    else:
        half = [[j % c for j in i] for i in exponent(a, b // 2, c)]
        return [[j % c for j in i] for i in square(half, half, c)]

N, B = map(int, input().split())
original_matrix = [list(map(int, input().split())) for i in range(N)]
for i in exponent(original_matrix, B, 1000):
    for j in i: print(j, end = ' ')
    print()