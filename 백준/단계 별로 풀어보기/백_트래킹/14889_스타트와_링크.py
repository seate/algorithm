from itertools import combinations
import sys
input = sys.stdin.readline
IP = lambda: map(int, input().split())

def solve():
    N = int(input())
    weight = [list(IP()) for i in range(N)]
    N_set = set(range(N))
    half_N = N // 2
    MIN = float("inf")
    
    for i in combinations(range(N), N // 2):
        team1 = set(i)
        team2 = list(N_set - team1)
        team1 = list(team1)
        
        present_differ = 0
        
        for i in range(half_N - 1):
            for j in range(i + 1, half_N):
                present_differ += (weight[team1[i]][team1[j]] + weight[team1[j]][team1[i]]) - (weight[team2[i]][team2[j]] + weight[team2[j]][team2[i]])
        
        if abs(present_differ) < MIN: MIN = abs(present_differ)
    
    print(MIN)

def fastest_solve():
    N = int(input())
    horizontal_weight = [list(IP()) for i in range(N)]
    vertical_weight = list(zip(*horizontal_weight))
    new_weight = [sum(horizontal_weight[i]) + sum(vertical_weight[i]) for i in range(N)]
    half_all_sum = sum(new_weight) // 2
    
    MIN = float("inf")
    for i in combinations(new_weight[:-1], N // 2):
        present_differ = abs(half_all_sum - sum(i))
        if present_differ < MIN: MIN = present_differ
    
    print(MIN)
    
if "__main__" == __name__:
    #solve()
    fastest_solve()