import sys
sys.setrecursionlimit(10 ** 8)
input = sys.stdin.readline

def BFS(present_list):
    
    for idx in range(1000010):
        list_for_next = []
        
        for h, y, x in present_list:
            if y != 0 and command[h][y - 1][x] == 0:
                list_for_next.append([h, y - 1, x])
                command[h][y - 1][x] = 1
            
            if y != N - 1 and command[h][y + 1][x] == 0:
                list_for_next.append([h, y + 1, x])
                command[h][y + 1][x] = 1
            
            if x != 0 and command[h][y][x - 1] == 0:
                list_for_next.append([h, y , x - 1])
                command[h][y][x - 1] = 1
            
            if x != M - 1 and command[h][y][x + 1] == 0:
                list_for_next.append([h, y, x + 1])
                command[h][y][x + 1] = 1
            
            if h != 0 and command[h - 1][y][x] == 0:
                list_for_next.append([h - 1, y, x])
                command[h - 1][y][x] = 1
            
            if h != H - 1 and command[h + 1][y][x] == 0:
                list_for_next.append([h + 1, y, x])
                command[h + 1][y][x] = 1
        
        if not list_for_next: break
        present_list = list_for_next[:]
    
    return idx

M, N, H = map(int, input().split())
command = [[list(map(int, input().split())) for j in range(N)] for i in range(H)]
initial_list, isit = [], True


for h in range(H):
    for y in range(N):
        for x in range(M):
            if command[h][y][x] == 1: initial_list.append([h, y, x])


result = BFS(initial_list)

for it in command:
    for it2 in it:
        if 0 in it2:
            isit = False
            break

print(result) if isit else print(-1)