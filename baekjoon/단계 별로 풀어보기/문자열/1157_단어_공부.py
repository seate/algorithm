import sys
input = sys.stdin.readline
IP = lambda: map(int, sys.stdin.readline().split())

def solve():
    word = input().rstrip().upper()
    counter = [word.count(chr(i)) for i in range(65, 91)]
    
    MAX = max(counter)
    print("?" if 1 < counter.count(MAX) else chr(counter.index(MAX) + 65))
    
if "__main__" == __name__: solve()