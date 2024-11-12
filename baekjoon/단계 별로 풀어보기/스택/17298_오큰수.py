import sys
input = sys.stdin.readline
IP = lambda: map(int, input().split())

def solve():
    N = int(input())
    members = list(IP())
    stack = []
    for i, member in zip(range(N - 1, -1, -1), members[::-1]):
        while stack and stack[-1] <= member: stack.pop()
        members[i] = str(stack[-1]) if stack else '-1'
        stack += [member]
    print(' '.join(members))

if __name__ == '__main__': sys.exit(solve())