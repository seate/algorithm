import sys
input = sys.stdin.readline
IP = lambda: map(int, input().split())

def general_case():
    MOD = 1000000007

    def square(first_matrix, second_matrix):
        result_matrix = [[0 for j in range(N)] for i in range(N)]
        for i in range(N):
            for j in range(N):
                for k in range(N): result_matrix[i][j] += (first_matrix[i][k] * second_matrix[k][j]) % MOD
        return [[j % MOD for j in i] for i in result_matrix]
    
    def exponent(a, b):
        if b == 1: return original_matrix
        elif b % 2 == 1: return square(exponent(a, b - 1), original_matrix)
        else:
            half = [[j % MOD for j in i] for i in exponent(a, b // 2)]
            return [[j % MOD for j in i] for i in square(half, half)]
    
    N, B = 2, int(input())
    original_matrix = [[1, 1], [1, 0]]
    print(exponent(original_matrix, B)[0][1])
    
if "__main__" == __name__: exact_solve()