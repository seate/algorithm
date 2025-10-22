def fill5(visit, peaks):
    UP, LEFT, RIGHT, DOWN = peaks
    
    d1 = LEFT[0] - UP[0]
    d2 = RIGHT[0] - UP[0]
    
    for d in range(d1 + 1): #UP -> LEFT
        cury = UP[0] + d
        curx = UP[1] - d
        
        visit[cury][curx] = 5
    
    for d in range(d2 + 1): #UP -> RIGHT
        cury = UP[0] + d
        curx = UP[1] + d
        
        visit[cury][curx] = 5
    
    
    for d in range(d2 + 1): #LEFT -> DOWN
        cury = LEFT[0] + d
        curx = LEFT[1] + d
        
        visit[cury][curx] = 5
    
    for d in range(d1 + 1): #RIGHT -> DOWN
        cury = RIGHT[0] + d
        curx = RIGHT[1] - d
        
        visit[cury][curx] = 5


N = int(input())

m = [[0] * (N + 1)]
for i in range(N):
    m.append([0] + list(map(int, input().split())))

totalCount = sum(sum(i) for i in m)

realAnswer = 99999999999999999999
for y in range(1, N + 1):
    for x in range(1, N + 1):
        for d1 in range(1, N + 1):
            for d2 in range(1, N + 1):
                #if not ((x + d1 + d2 <= N) and (1 <= y - d1) and (y + d2 <= N)): continue
                if not ((y + d1 + d2 <= N) and (1 <= x - d1) and (x + d2 <= N)): continue
                
                visit = [[0] * (N + 1) for _ in range(N + 1)]
                
                UP = [y, x]
                LEFT = [y + d1, x - d1]
                RIGHT = [y + d2, x + d2]
                DOWN = [y + d1 + d2, x - d1 + d2]
                
                peaks = [UP, LEFT, RIGHT, DOWN]
                
                fill5(visit, peaks)
                
                answers = [0] * 5
                
                # 1
                for vy in range(1, LEFT[0]):
                    for vx in range(1, UP[1] + 1):
                        if visit[vy][vx] == 5: break
                        
                        answers[0] += m[vy][vx]
                
                # 2
                for vy in range(1, RIGHT[0] + 1):
                    for vx in range(N, UP[1], -1):
                        if visit[vy][vx] == 5: break
                        
                        answers[1] += m[vy][vx]
                
                # 3
                for vy in range(LEFT[0], N + 1):
                    for vx in range(1, DOWN[1]):
                        if visit[vy][vx] == 5: break
                        
                        answers[2] += m[vy][vx]
                
                # 4
                for vy in range(RIGHT[0] + 1, N + 1):
                    for vx in range(N, DOWN[1] - 1, -1):
                        if visit[vy][vx] == 5: break
                        
                        answers[3] += m[vy][vx]
                
                # 5
                answers[4] = totalCount - sum(answers)
                
                realAnswer = min(realAnswer, max(answers) - min(answers))#"""
                
                
print(realAnswer)