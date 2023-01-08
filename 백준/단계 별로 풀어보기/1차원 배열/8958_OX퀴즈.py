import sys
input = sys.stdin.readline
IP = lambda: map(int, sys.stdin.readline().split())

def solve():
    for T in range(int(input())):
        command = input().rstrip()
        plus_score = 1; result_score = 0
        
        for each in command:
            if each == 'O':
                result_score += plus_score
                plus_score += 1
            else: plus_score = 1
        print(result_score)
    
if "__main__" == __name__: solve()