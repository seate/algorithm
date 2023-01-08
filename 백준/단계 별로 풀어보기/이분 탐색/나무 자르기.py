length, M = map(int, input().split())
value = list(map(int, input().split()))
value.sort()

present = value[-1] // 2 - 1
jumper =  present // 2 if not present == 1 else 1
big, small = 0, 0

while True:
    gather = sum([value[i] - present for i in range(length) if value[i] > present])
    
    if gather != M:
        present += (jumper if M < gather else -1 * jumper)
        
        if jumper == 1:
            if not small and gather < M: small = big + 1
            elif not big and M < gather: big = small + 1
            
            if big == 2:
                present -= 1
                break
        
        else: jumper = jumper // 2
    
    else: break

print(present)