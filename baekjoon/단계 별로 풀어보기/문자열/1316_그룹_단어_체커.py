import sys
input = sys.stdin.readline
IP = lambda: map(int, sys.stdin.readline().split())

def solve():
    result = 0
    
    for T in range(int(input())):
        word = input().rstrip()
        check = word[0]
        isit = True
        visited = set([word[0]])
        
        for letter in word:
            if check != letter:
                if letter in visited:
                    isit = False
                    break;
                
                visited.add(letter)
                check = letter
        
        result += isit
    
    print(result)

def other_solve():
    result = 0
    for T in range(int(input())):
        word = input().rstrip()
        result += (list(word) == sorted(word, key = word.find))
    print(result)
    
if "__main__" == __name__:
    #solve()
    other_solve()