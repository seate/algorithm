import sys
sys.setrecursionlimit(10 ** 8)
input = sys.stdin.readline

def BFS(present_list):
    
    for idx in range(1000010):
        list_for_next = []
        
        for y, x in present_list:
            if y != 0 and command[y - 1][x] == 0:
                list_for_next.append([y - 1, x])
                command[y - 1][x] = 1
            
            if y != N - 1 and command[y + 1][x] == 0:
                list_for_next.append([y + 1, x])
                command[y + 1][x] = 1
            
            if x != 0 and command[y][x - 1] == 0:
                list_for_next.append([y , x - 1])
                command[y][x - 1] = 1
            
            if x != M - 1 and command[y][x + 1] == 0:
                list_for_next.append([y, x + 1])
                command[y][x + 1] = 1
        
        if not list_for_next: break
        present_list = list_for_next[:]
    
    return idx

M, N = map(int, input().split())
command = [list(map(int, input().split())) for i in range(N)]
initial_list, isit = [], True

for fir in range(len(command)):
    for sec in range(len(command[fir])):
        if command[fir][sec] == 1: initial_list.append([fir, sec])

result = BFS(initial_list)

for it in command:
    if 0 in it:
        isit = False
        break

print(result) if isit else print(-1)