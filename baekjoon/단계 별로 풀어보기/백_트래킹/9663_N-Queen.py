import sys
input = sys.stdin.readline
IP = lambda: map(int, input().split())

def solve():
    def recursion(y = 0):
        for x in range(N):
            #퀸을 놓을 때
            if not board[y][x]:
                #가능해서 count += 1
                if y == N - 1:
                    count[0] += 1
                    return
                
                #세로
                for i in range(y + 1, N): board[i][x] += 1
                
                #오른쪽 아래
                py = y; px = x
                while py < N and px < N:
                    board[py][px] += 1
                    py += 1; px += 1
                
                #왼쪽 아래
                py = y; px = x
                while py < N and 0 <= px:
                    board[py][px] += 1
                    py += 1; px -= 1
                
                #실행
                recursion(y + 1)
                
                #세로
                for i in range(y + 1, N): board[i][x] -= 1
                
                #오른쪽 아래
                py = y; px = x
                while py < N and px < N:
                    board[py][px] -= 1
                    py += 1; px += 1
                
                #왼쪽 아래
                py = y; px = x
                while py < N and 0 <= px:
                    board[py][px] -= 1
                    py += 1; px -= 1
    
    
    N = int(input())
    board = [[0] * N for i in range(N)]
    count = [0]
    
    recursion()
    print(count[0])

def fastest_solve(): print([0,1,0,0,2,10,4,40,92,352,724,2680,14200,73712,365596][int(input())])
    
if "__main__" == __name__:
    solve()
    #fastest_solve()