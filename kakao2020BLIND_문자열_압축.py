def solution(s):
    def flow(l):
        result = 0
        idx = 0
        stack = 1
        
        while True:
            if s[idx:idx + l] == s[idx + l:idx + (l * 2)]: stack += 1
            else:
                result += (len(str(stack)) if stack != 1 else 0) + l
                stack = 1            
            
            idx += l
            
            if len(s) < idx + (l * 2):
                result += (len(str(stack)) if stack != 1 else 0) + l
                result += len(s) - (idx + l)
                break
        
        return result
        

    answer = len(s)
    for i in range(1, len(s)): answer = min(answer, flow(i))    
    
    return answer