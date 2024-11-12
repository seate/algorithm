import sys
input = sys.stdin.readline
IP = lambda: map(int, input().split())

def solve():
    def recursion(calculated, depth = 1):
        if depth == N:
            if Mm[0] < calculated: Mm[0] = calculated
            if calculated < Mm[1]: Mm[1] = calculated
            return
        
        if oper[0]:
            oper[0] -= 1
            recursion(calculated + nums[depth], depth + 1)
            oper[0] += 1
        if oper[1]:
            oper[1] -= 1
            recursion(calculated - nums[depth], depth + 1)
            oper[1] += 1
        if oper[2]:
            oper[2] -= 1
            recursion(calculated * nums[depth], depth + 1)
            oper[2] += 1
        if oper[3]:
            oper[3] -= 1
            recursion(int(calculated / nums[depth]), depth + 1)
            oper[3] += 1
    
    
    N = int(input())
    nums = list(IP())
    oper = list(IP())
    Mm = [-float("inf"), float("inf")]
    
    recursion(nums[0])
    
    print('\n'.join(map(str, Mm)))
    
if "__main__" == __name__: solve()