import sys
input = sys.stdin.readline
IP = lambda: map(int, sys.stdin.readline().split())

def solve():
    word = input().rstrip()
    alpha = ["ABC", "DEF", "GHI", "JKL", "MNO", "PQRS", "TUV", "WXYZ"]
    result = 0
    
    for letter in word:
        for i in range(8):
            if letter in alpha[i]: result += (i + 3)
    
    print(result)
    
if "__main__" == __name__: solve()