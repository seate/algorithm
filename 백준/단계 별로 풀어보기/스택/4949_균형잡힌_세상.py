import sys
input = sys.stdin.readline
IP = lambda: map(int, input().split())

def solve():
    while True:
        string = input().rstrip()
        if string == '.': break
        stack = []
        isit = True
        
        for s in string:
            if s == "(": stack.append(1)
            elif s == ")":
                if stack and stack[-1] == 1: stack.pop()
                else: isit = False; break
            elif s == "[": stack.append(2)
            elif s == "]":
                if stack and stack[-1] == 2: stack.pop()
                else: isit = False; break
        
        print("yes" if isit and not stack else "no")
    
if "__main__" == __name__: solve()