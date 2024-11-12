import sys
input = sys.stdin.readline
IP = lambda: map(int, sys.stdin.readline().split())

def solve():
    croatia = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
    word = input().rstrip()
    
    for letter in croatia: word = word.replace(letter, '*')
    
    print(word)
    
    print(len(word))
    
if "__main__" == __name__: solve()