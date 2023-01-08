import sys
input = sys.stdin.readline
IP = lambda: map(int, input().split())

def solve():
    N = int(input())
    destination = [int(input()) for i in range(N)]
    
    to_stack = []; from_stack = list(range(N, 0, -1))
    result = []; index = 0; isit = True
    
    while index < N:
        if not to_stack or to_stack[-1] < destination[index]:
            result.append('+')
            to_stack.append(from_stack.pop())
        
        elif to_stack[-1] == destination[index]:
            to_stack.pop()
            result.append('-')
            index += 1
        
        elif destination[index] < to_stack[-1]: isit = False; break
    
    print('\n'.join(result) if isit else "NO")
    
if "__main__" == __name__: solve()