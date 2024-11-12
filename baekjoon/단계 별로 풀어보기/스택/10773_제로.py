import sys
input = sys.stdin.readline
IP = lambda: map(int, input().split())

def solve():
    stack = []
    commands = [int(input()) for i in range(int(input()))]
    
    for i in commands:
        if i: stack += [i]
        else: stack.pop()
    
    print(sum(stack))
    
if "__main__" == __name__: solve()