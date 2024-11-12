import sys
input = sys.stdin.readline
IP = lambda: map(int, input().split())

def recursion(depth = 0):
    if depth == Zero_length:
        print("\n".join([' '.join(map(str, line)) for line in board]))
        sys.exit(0)
    
    x, y = zero[depth]
    start_x = (x // 3) * 3
    start_y = (y // 3) * 3
    
    #가능여부
    possible = [True] * 10
    #직선
    for i in range(9):
        if board[y][i]: possible[board[y][i]] = False
        if board[i][x]: possible[board[i][x]] = False
    #3X3 박스
    for p_y in range(start_y, start_y + 3):
        for p_x in range(start_x, start_x + 3):
            if board[p_y][p_x]: possible[board[p_y][p_x]] = False
    #다음 재귀
    for i in range(1, 10):
        if possible[i]:
            board[y][x] = i
            recursion(depth + 1)

board = [list(IP()) for _ in range(9)]
zero = [(x, y) for y in range(9) for x in range(9) if not board[y][x]]
Zero_length = len(zero)
recursion()