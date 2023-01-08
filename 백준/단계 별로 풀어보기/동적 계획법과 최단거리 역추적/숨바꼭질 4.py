import sys

def solve():
    N, K = map(int, sys.stdin.readline().split())
    if K <= N:
        print(N - K)
        for i in range(N, K - 1, -1): print(i, end = ' ') #메모리 중시
        #print(' '.join(map(str, list(range(N, K - 1, -1))))) 시간 중시 
        return
    present = [N]
    trace = [-1] * 100001; trace[N] = -2
    idx = 0
    
    while True:
        list_for_next = []
        while present:
            locate = present.pop()
            
            if locate == K:
                trace_result = []
                while K != -2: trace_result.append(K); K = trace[K]
                print(idx)
                print(' '.join(map(str, trace_result[::-1])))
                return 
            
            if 0 < locate and trace[locate - 1] == -1:
                list_for_next.append(locate - 1)
                trace[locate - 1] = locate
            
            if K < locate: continue
            
            if locate < 100000 and trace[locate + 1] == -1:
                list_for_next.append(locate + 1)
                trace[locate + 1] = locate
            
            if locate <= 50000 and trace[locate * 2] == -1:
                list_for_next.append(locate * 2)
                trace[locate * 2] = locate
        
        present = list_for_next
        idx += 1
    
if "__main__" == __name__: solve()