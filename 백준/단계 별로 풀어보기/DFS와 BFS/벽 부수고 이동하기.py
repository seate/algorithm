import sys
input = sys.stdin.readline

def BFS(present_list):
    limit, dy, dx, idx = [0, Y - 1, 0, X - 1], [-1, 1, 0, 0], [0, 0, -1, 1], 1
    
    while True:
        list_for_next = []
        for breakable, y , x in present_list:
            if y == limit[1] and x == limit[3]: return idx
            xy = [y, y, x, x]
            
            for i in range(4):
                if xy[i] != limit[i] and wall[y + dy[i]][x + dx[i]] <= breakable and not visited[breakable][y + dy[i]][x + dx[i]]:
                    list_for_next.append([wall[y + dy[i]][x + dx[i]] < breakable, y + dy[i], x + dx[i]])
                    for j in range(breakable + 1): visited[j][y + dy[i]][x + dx[i]] = True
        
        idx += 1
        if not list_for_next: return -1
        present_list = list_for_next[:]


Y, X = map(int, input().split())
wall = [list(map(int, input().rstrip('\n'))) for i in range(Y)]
visited = [[[False] * X for j in range(Y)] for i in range(2)]
for i in range(2): visited[i][0][0] = True
print(BFS([[True, 0, 0]])) if not Y == X == 1 else print(1)