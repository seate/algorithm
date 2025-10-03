from collections import defaultdict

def conv(stime):
    h, m = map(int, stime.split(":")) 
    
    return h * 60 + m

def solution(fees, records):
    defaultTime, defaultfee, unitTime, unitFee = fees
    
    def cal(duTime):
        duTime -= defaultTime
        resultFee = defaultfee
        
        if duTime <= 0: return resultFee
        
        resultFee += ((duTime // unitTime) + ((duTime % unitTime) != 0)) * unitFee
        
        return resultFee
    
    resultTime = defaultdict(int)
    log = dict()
    for r in records:
        stime, num, act = r.split()
        itime = conv(stime)
        
        if act == "IN": log[num] = itime
        else:
            resultTime[num] += itime - log[num]
            log.pop(num)
    
    for num, itime in log.items():
        resultTime[num] += conv("23:59") - log[num]
        
    return [cal(t) for n, t in sorted(list(resultTime.items()))]