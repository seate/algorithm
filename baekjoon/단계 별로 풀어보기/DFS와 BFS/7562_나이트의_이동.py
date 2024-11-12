from sys import stdin
from collections import deque
input = stdin.readline
IP = lambda: map(int, input().split())

def solve():
    Nx = [1, 2, 2, 1, -1, -2, -2, -1]
    Ny = [2, 1, -1, -2, -2, -1, 1, 2]
    
    for T in range(int(input())):
        board_length = int(input())
        initial_locate = list(IP())
        destination = list(IP())
        board = [[-1] * board_length for i in range(board_length)]; board[initial_locate[0]][initial_locate[1]] = 0
        
        que = deque([initial_locate])
        while que:
            y, x = que.popleft()
            if [y, x] == destination: print(board[y][x]); break
            
            for i in range(8):
                nx, ny = x + Nx[i], y + Ny[i]
                if -1 < nx < board_length and -1 < ny < board_length and board[ny][nx] == -1:
                    board[ny][nx] = board[y][x] + 1
                    que += [[ny, nx]]

def other_solve():
    dx = [-2, -2, -1, -1, 1, 1, 2, 2]
    dy = [-1, 1, -2, 2, -2, 2, -1, 1]
    
    def bfs_bound(bd, start, end):
        if start == end: return 0
        que = [start]; visited = {start}; m = 1
        while True:
            new_que = []
            for x, y in que:
                for i, j in zip(dx, dy):
                    nx, ny = x + i, y + j
                    if 0 <= nx < bd and 0 <= ny < bd:
                        new = nx, ny
                        if new not in visited:
                            visited.add(new)
                            new_que += [new]
            if end in visited: return m
            m += 1
            que = new_que
    
    def bfs(p):
        if p == (0, 0): return 0
        start = (0, 0); que = [start]; visited = {start}
        
        for m in range(1, 10):
            new_que = []
            for x, y in que:
                for i, j in zip(dx, dy):
                    new = x + i, y + j
                    if new not in visited:
                        visited.add(new)
                        new_que += [new]
            if p in visited: return m
            que = new_que
    
    def manual(x, y):
        i = 0
        while 5 <= x or 5 <= y:
            x, y = (x - 2, abs(y - 1)) if y < x else (abs(x - 1), y - 2)
            i += 1
        return i + bfs((x, y))
    
    for _ in range(int(input())):
        bd = int(input())
        x1, y1 = IP()
        x2, y2 = IP()
        x, y = abs(x1 - x2), abs(y1 - y2)
        if 5 <= x or 5 <= y: print(manual(x, y))
        else: print(bfs_bound(bd, (x1, y1), (x2, y2)))
    
if "__main__" == __name__: other_solve()