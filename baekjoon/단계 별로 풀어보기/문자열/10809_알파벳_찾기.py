import sys
input = sys.stdin.readline
IP = lambda: map(int, sys.stdin.readline().split())

def solve():
    locate = [-1] * 26
    word = input().rstrip()
    
    for i in range(len(word)):
        if locate[ord(word[i]) - 97] == -1: locate[ord(word[i]) - 97] = i
    
    print(*locate)

def other_solve():
    string = input()
    print(*[string.find(i) for i in "abcdefghijklmnopqrstuvwxyz"])
    
if "__main__" == __name__: other_solve()