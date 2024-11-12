import sys
input = sys.stdin.readline
IP = lambda: map(int, input().split())

def solve():
    people_box = [[0] * 15 for i in range(15)]
    people_box[1] = [i * (i + 1) // 2 for i in range(15)]
    
    for i in range(2, 15):
        for j in range(1, 15): people_box[i][j] = people_box[i - 1][j] + people_box[i][j - 1]
    
    for T in range(int(input())): print(people_box[int(input())][int(input())])
    
if "__main__" == __name__: solve()