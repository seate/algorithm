from collections import deque
import sys
input = sys.stdin.readline
IP = lambda: map(int, input().split())

def solve():
    que = deque()
    result = []
    
    for i in range(int(input())):
        c = input().split()
        j = c[0][0]
        
        try:
            if j == "p":
                if c[0][1] == "u": que.append(c[1])
                else: result.append(que.popleft())
            elif j == "s": result.append(len(que))
            elif j == "e": result.append(int(not que))
            elif j == "f": result.append(que[0])
            else: result.append(que[-1])
        except: result.append("-1")
    
    print("\n".join(map(str, result)))
    
if "__main__" == __name__: solve()