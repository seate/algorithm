import collections
import sys
input = sys.stdin.readline
IP = lambda: map(int, sys.stdin.readline().split())
MOD = 10000

def solve():
    def BFS(start):
        q = collections.deque([start])
        while not trace[d]:
            present = q.popleft()
            next_locate = present * 2
            if MOD <= next_locate:
                next_locate %= MOD
                if not trace[next_locate]:
                    trace[next_locate] = "DM"
                    q.append(next_locate)
            elif not trace[next_locate]:
                trace[next_locate] = "D"
                q.append(next_locate)
            
            next_locate = (present - 1 if present else 9999)
            if not trace[next_locate]:
                trace[next_locate] = "S"
                q.append(next_locate)
            
            next_locate = (present % 1000) * 10 + (present // 1000)
            if not trace[next_locate]:
                trace[next_locate] = "L"
                q.append(next_locate)
            
            next_locate = (present % 10) * 1000 + (present // 10)
            if not trace[next_locate]:
                trace[next_locate] = "R"
                q.append(next_locate)
    
    for T in range(int(input())):
        s, d = IP()
        trace = [False] * 10001; trace[s] = True
        result = []
        BFS(s)
        
        while s != d:
            result.append(trace[d][0])
            if trace[d] == "DM": d = (d + 10000) // 2
            elif trace[d] == "D": d //= 2
            elif trace[d] == "S": d = (d + 1) % MOD
            elif trace[d] == "L": d = (d % 10) * 1000 + d // 10
            elif trace[d] == "R": d = (d % 1000) * 10 + (d // 1000)
        
        print(''.join(result[::-1]))
    
if "__main__" == __name__: solve()