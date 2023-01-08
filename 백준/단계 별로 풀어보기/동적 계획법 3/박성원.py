import math
input = __import__('sys').stdin.readline

def solve():
    N = int(input())
    nums = [int(input()) for i in range(N)]
    K = int(input())
    #rests[i번째 수][앞에 올 수 있는 모든 나머지 경우의 수(0 ~ K - 1)] = (int("앞에 올 수 있는 모든 나머지 경우의 수(0 ~ K - 1)" + "i번째 수") % K)
    rests = [[(j * pow(10, len(str(nums[i]))) + nums[i]) % K for j in range(K)] for i in range(N)]
    
    #dp[수가 있는지 없는지 비트마스크로 표헌][(늘어놓은 수 % K)(= 나머지)] = 있는 수들을 늘어놓을 때 나머지가 같게 되는 경우의 수
    dp = [[0] * K for _ in range(1 << N)]
    dp[0][0] = 1
    
    
    
    for i in range(1 << N):
        for j in range(N):
            if i & (1 << j): continue #i에 이미 j번째 수가 포함되어 있는 경우 건너뛴다
            for l in range(K):
                dp[i | (1 << j)][rests[j][l]] += dp[i][l]
    
    numerator = dp[(1 << N) - 1][0]
    dominator = math.factorial(N)
    G = math.gcd(numerator, dominator)
    
    print("%d/%d" % (numerator // G, dominator // G))
    
if "__main__" == __name__: solve()