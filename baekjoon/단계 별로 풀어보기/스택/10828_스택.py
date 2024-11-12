import sys
input = sys.stdin.readline
IP = lambda: map(int, input().split())

def solve():
    stack = []
    length = 0
    for T in range(int(input())):
        command = input().split()
        if command[0][0] == 'p':
            if command[0][1] == 'u': stack += [command[1]]; length += 1
            elif stack: print(stack.pop()); length -= 1
            else: print('-1')
        
        elif command[0][0] == 's': print(length)
        
        elif command[0][0] == 'e': print(int(not stack))
        
        else: print(stack[-1] if stack else '-1')
    
if "__main__" == __name__: solve()