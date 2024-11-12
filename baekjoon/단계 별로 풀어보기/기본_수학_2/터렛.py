import math


T = int(input())
for fir_again in range(T):
    inlist = []
    inlist = input().split()
    for again in inlist:
        again = int(again)
    x1 = int(inlist[0])
    y1 = int(inlist[1])
    r1 = int(inlist[2])
    x2 = int(inlist[3])
    y2 = int(inlist[4])
    r2 = int(inlist[5])
    distance = math.sqrt(abs(x2 - x1) ** 2 + abs(y2 - y1) ** 2)
    
    
    if x1 == x2 and y1 == y2 and r1 == r2:  print("-1") #일치하는 경우
    
    else:   #일치하지 않는 경우
        if distance + min(r1, r2) < max(r1, r2):    #원이 완전 포함되는 경우
            print("0")
        #elif distance < r1 or distance < r2:
        elif distance == max(r1, r2) - min(r1, r2):
            print("1")
        else:   #원 안에 중심이 포함되지 않는 경우
            if distance < r1 + r2:
                print("2")
            elif distance == r1 + r2:
                print("1")
            else:
                print("0")