import sys
input = sys.stdin.readline
IP = lambda: map(int, input().split())

def solve():
    for T in range(int(input())):
        string = input().rstrip()
        count = 0
        
        for s in string:
            if s == "(": count += 1
            else: count -= 1
            
            if count < 0: break
        
        print("YES" if count == 0 else "NO")
    
if "__main__" == __name__: solve()