def conv(c):
    return 1 if c == "(" else -1

def isr(s):
    dp = 0
    for i in range(len(s)):
        dp += conv(s[i])
        if dp < 0: return False
    
    return dp == 0
        
def rvs(s):
    def __rvs(c): return ["(", ")"][c == "("]

    return ''.join(map(__rvs, s))
    

def flow(s):
    if len(s) == 0: return ""
    
    cnt = conv(s[0])
    idx = 1
    while cnt != 0:
        cnt += conv(s[idx])
        idx += 1
    
    
    if isr(s[:idx]):
        return s[:idx] + flow(s[idx:])
    else:
        return "(" + flow(s[idx:]) + ")" + rvs(s[1:idx - 1])

    

def solution(p):
    return flow(p)