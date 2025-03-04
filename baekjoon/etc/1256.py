MAX = 1000000000

def solve():
    N, M, K = map(int, input().split())

    dp =[[0] * 101 for _ in range(101)]
    for i in range(101):
        dp[0][i] = 1
        dp[i][0] = 1

    for i in range(1, N + 1):
        for j in range(1, M + 1):
            dp[i][j] = dp[i][j - 1] + dp[i - 1][j]
            if MAX < dp[i][j]: dp[i][j] = MAX

    if dp[N][M] < K:
        print("-1")
        return

    A = N
    Z = M
    result = []
    for _ in range(N + M):
        if A == 0:
            result.append("z")
            Z -= 1
        elif Z == 0:
            result.append("a")
            A -= 1
        elif K <= dp[A - 1][Z]:
            result.append("a")
            A -= 1
        else :
            result.append("z")
            K -= dp[A - 1][Z]
            Z -= 1

    print("".join(result))

solve()