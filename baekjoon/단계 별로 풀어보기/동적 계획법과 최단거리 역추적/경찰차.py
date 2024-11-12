import sys
input = sys.stdin.readline
IP = lambda: map(int, sys.stdin.readline().split())
sys.setrecursionlimit(10 ** 9)

def recursion_solve(): #much_worse_sovle
    def recur(n1, n2):
        if n1 == W - 1 or n2 == W - 1: return 0
        if dp[n1][n2]: return dp[n1][n2][0]
        accident = (n1 if n2 < n1 else n2) + 1
        A = recur(accident, n2) + (abs(accident[n1][0] - accident[accident][0]) + abs(accident[n1][1] - accident[accident][1]))
        B = recur(n1, accident) + (abs(accident[n2][0] - accident[accident][0]) + abs(accident[n2][1] - accident[accident][1]))
        dp[n1][n2] = [A, 1] if A < B else [B, 2]
        return dp[n1][n2][0]
    
    N = int(input()); W = int(input()) + 2
    accident = [(1, 1), (N, N)] + [tuple(IP()) for i in range(W - 2)]
    dp = [[0] * W for i in range(W)]; p_l = [None, 0, 1]
    
    print(recur(0, 1))
    for present_trace in range(2, W):
        print(dp[p_l[1]][p_l[2]][1])
        p_l[dp[p_l[1]][p_l[2]][1]] = present_trace

def double_for_solve(): #much better
    N = int(input()); W = int(input())
    accident = [(1, 1), (N, N)] + [tuple(IP()) for i in range(W)]
    dp = [[0] * (W + 2) for i in range(W + 2)]; trace = [[0] * (W + 2) for i in range(W + 2)]
    
    for j in range(W, 0 , -1):
        for i in range(j):
            I = abs(accident[i][0] - accident[j + 1][0]) + abs(accident[i][1] - accident[j + 1][1]) + dp[j][j + 1]
            J = abs(accident[j + 1][0] - accident[j][0]) + abs(accident[j + 1][1] - accident[j][1]) + dp[i][j + 1]
            if I < J: dp[i][j] = I; trace[i][j] = i
            else: dp[i][j] = J; trace[i][j] = j
    
    trace_result = [1, 2]; i = 0
    for j in range(1, W + 1):
        if trace[i][j] == i:
            trace_result.append(trace_result[i])
            i = j
        else: trace_result.append(trace_result[j])
    
    print(dp[0][1])
    print('\n'.join(map(str, trace_result[2:])))
    
if "__main__" == __name__: double_for_solve()