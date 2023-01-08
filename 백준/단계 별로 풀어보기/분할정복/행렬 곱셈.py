N, M = map(int, input().split())
first_matrix = [list(map(int, input().split())) for i in range(N)]
M, K = map(int, input().split())
second_matrix = [list(map(int, input().split())) for i in range(M)]
result_matrix = [[0 for j in range(K)] for i in range(N)]


for i in range(N):
    for j in range(K):
        for k in range(M): result_matrix[i][j] += (first_matrix[i][k] * second_matrix[k][j])

for i in result_matrix:
    for j in i: print(j, end = ' ')
    print()