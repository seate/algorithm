#문제가 매우 더러워서 최적화 안함

from collections import deque
import sys
input = sys.stdin.readline
IP = lambda: map(int, input().split())

def solve():
    def find_parent(search):
        if parent[search] < 0: return search
        parent[search] = find_parent(parent[search])
        return parent[search]
    
    Y, X = IP()
    board = [list(IP()) for i in range(Y)]
    
    isl_num = 2
    dy = [1, 0, -1, 0]
    dx = [0, 1, 0, -1]
    candidate = [[], [], [], []]
    
    for y in range(Y):
        for x in range(X):
            #미부여된 섬에 접촉하면
            if board[y][x] == 1:
                #bfs로 섬 전체에 번호를 부여한다
                board[y][x] = isl_num
                que = deque([(y, x)])
                while que:
                    py, px = que.popleft()
                    condition = [py + 1 < Y, px + 1 < X, py, px]
                    for i in range(4):
                        #진행가능한 경우
                        if condition[i]:
                            #다음 타일이 0이라서 다리 놓는 지점 후보에 저장
                            if not board[py + dy[i]][px + dx[i]]:
                                candidate[i].append((py + dy[i], px + dx[i]))
                            #다음 타일이 1이라서 연결된 섬이면 저장
                            elif board[py + dy[i]][px + dx[i]] == 1:
                                board[py + dy[i]][px + dx[i]] = isl_num
                                que.append((py + dy[i], px + dx[i]))
                isl_num += 1
    
    edge = [dict() for i in range(isl_num)]
    
    #다리 놓기
    for i in range(4):
        for initial_y, initial_x in candidate[i]:
            length = 0
            present_y, present_x = initial_y, initial_x
            
            #length를 늘리며 다리 놓기
            while (0 <= present_y < Y and 0 <= present_x < X) and not board[present_y][present_x]:
                length += 1
                present_y += dy[i]
                present_x += dx[i]
            
            #갱신하지 않을 때:
            #board 범위를 초과해서 끝났을 경우 or length < 2 or 진행한 곳이 같은 섬이었을 경우
            if ((present_y < 0 or Y <= present_y) or (present_x < 0 or X <= present_x)) or length < 2 or board[present_y][present_x] == board[initial_y][initial_x]: continue
            
            
            
            s, b = (board[initial_y - dy[i]][initial_x - dx[i]], board[present_y][present_x]) if board[initial_y - dy[i]][initial_x - dx[i]] < board[present_y][present_x] else (board[present_y][present_x], board[initial_y - dy[i]][initial_x - dx[i]])
            if b in edge[s]:
                if length < edge[s][b]: edge[s][b] = length
            else: edge[s][b] = length
    
    result_cost = 0; sorted_edge = []
    parent = [-1] * isl_num
    for start in range(2, isl_num):
        for end in edge[start]: sorted_edge.append((edge[start][end], start, end))
    sorted_edge.sort()
    
    for present_cost, start, end in sorted_edge:
        S = find_parent(start); E = find_parent(end)
        if S == E: continue
        elif parent[S] < parent[E]:
            parent[S] += parent[E]
            parent[E] = S
        else:
            parent[E] += parent[S]
            parent[S] = E
        
        result_cost += present_cost
    
    counter = 0
    for i in parent[2:]:
        if i < 0:
            counter += 1
            if 2 <= counter: break
    
    print(result_cost if counter < 2 else '-1')
    
if "__main__" == __name__: solve()