def solution(key, lock):
    M = len(key)
    N = len(lock)
    L = 2 * M + N
    
    def rotate(m):    
        newm = [[0] * M for _ in range(M)]
        
        for y in range(M):
            for x in range(M):
                newm[x][M - y - 1] = m[y][x]
        
        return newm
    
    
    def check():
        for i in range(N):
            for j in range(N):
                if dp[i + M][j + M] != 1: return False
        
        return True
    

    dp = [[0] * L for _ in range(L)]
    for y in range(N):
        for x in range(N):
            dp[y + M][x + M] = lock[y][x]
    
    
    for i in range(4):
        for y in range(L - M):
            for x in range(L - M):
                
                for i in range(M):
                    for j in range(M):
                        dp[y + i][x + j] += key[i][j]
                
                if check(): return True
                
                for i in range(M):
                    for j in range(M):
                        dp[y + i][x + j] -= key[i][j]
        
        if i == 3: break
        key = rotate(key)
    
    return False