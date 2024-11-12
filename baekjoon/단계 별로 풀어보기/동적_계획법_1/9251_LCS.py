import sys
input = sys.stdin.readline
IP = lambda: map(int, input().split())

def solve():
    word1 = input().rstrip()
    word2 = input().rstrip()
    LCS = [[0] * (len(word1) + 1) for i in range(len(word2) + 1)]
    
    for i in range(1, len(word2) + 1):
        for j in range(1, len(word1) + 1): LCS[i][j] = LCS[i - 1][j - 1] + 1 if word1[j - 1] == word2[i - 1] else (LCS[i - 1][j] if LCS[i][j - 1] < LCS[i - 1][j] else LCS[i][j - 1])
    
    print(LCS[-1][-1])
    
if "__main__" == __name__: solve()