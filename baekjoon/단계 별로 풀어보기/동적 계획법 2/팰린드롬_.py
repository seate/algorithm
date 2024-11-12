import math
import sys
input = sys.stdin.readline


length, data, number_of_quest, quest, executed = int(input()), list(map(int, input().split())), int(input()), [], []
dp = [[0 for j in range(length + 1)] for i in range(length + 1)]

for i in range(number_of_quest):
    a, b = map(int, input().split())
    quest.append([a - 1, b - 1])

middles = [(each[0] + each [1]) / 2 for each in quest]

for i in range(number_of_quest):
    if not middles[i] in executed:
        S, E = math.floor(middles[i]), math.ceil(middles[i])
        
        while S > -1 and E < length and data[S] == data[E]:
            dp[S][E] = 1
            S -= 1
            E += 1
        
        executed.append(middles[i])
    
    print(dp[quest[i][0]][quest[i][1]])
    
    
""" 풀이 2 재귀형 메모리 소모 감소, 시간 감소(훨씬)
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def is_palindrome(start, end):
    if dp[start][end] != -1: return dp[start][end]
    
    if end <= start + 1:
        dp[start][end] = int(data[start] == data[end])
        return dp[start][end]
    
    dp[start][end] = (1 if data[start] == data[end] and is_palindrome(start + 1, end - 1) == 1 else 0)
    return dp[start][end]


length, data, number_of_quest = int(input()), list(map(int, input().split())), int(input())
dp = [[-1] * (length + 1) for i in range(length + 1)]
for i in range(number_of_quest):
    start, end = map(int, input().split())
    print(is_palindrome(start - 1, end - 1))
"""