import sys
input = sys.stdin.readline
IP = lambda: map(int, input().split())

def solve():
    while True:
        word = input().rstrip('\n')
        if word == ".": break
        word_length = len(word)
        
        LPS = [0] * word_length
        length = 0; i = 1
        
        while i < word_length:
            if word[i] == word[length]:
                length += 1
                LPS[i] = length
                i += 1
            else:
                if length: length = LPS[length - 1]
                else: LPS[i] = 0; i += 1
        
        print('1' if word_length % (word_length - LPS[-1]) else word_length // (word_length - LPS[-1]))
    
if "__main__" == __name__: solve()