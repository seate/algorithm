from math import log
from sys import stdin

def solve():
    N = int(stdin.readline())
    board = [['*'] * N for i in range(N)]
    block_term = N
    term_length = N // 3
    repeat = 1
    
    while repeat != N:
        start_y = term_length
        for y in range(repeat):
            start_x = term_length
            for x in range(repeat):
                for s_y in range(start_y, start_y + term_length):
                    for s_x in range(start_x, start_x + term_length): board[s_y][s_x] = " "
                start_x += block_term
            start_y += block_term
        
        term_length //= 3
        block_term //= 3
        repeat *= 3
    
    print('\n'.join([''.join(line) for line in board]))

def other_solve():
    def concatenate(r1, r2): return [''.join(x) for x in zip(r1, r2, r1)]
    
    def star10(n):
        if n == 1: return ['*']
        n //= 3
        x = star10(n)
        a = concatenate(x, x)
        b = concatenate(x, [' ' * n] * n)
        
        return a + b + a
    
    print('\n'.join(star10(int(input()))))
    
if "__main__" == __name__:
    #solve()
    other_solve()