import sys
input = sys.stdin.readline
IP = lambda: map(int, input().split())

def solve():
    Y, X = IP()
    
    page = []    
    for curY in range(1, Y):
        count, *data = input().split()
        count = int(count)
        
        if count == 0: continue
        elif count == 1: page.append([count, int(data[0]), data[1]])
        else:
            data[0] = int(data[0])
            data[2] = int(data[2])
            
            if (data[1] == "R") and (data[3] == "R"): page.append([1, min(data[0], data[2]), "R"])
            elif (data[1] == "L") and (data[3] == "L"): page.append([1, max(data[0], data[2]), "L"])
            else: page.append([2, data[0], data[1], data[2], data[3]])
    
    
    curX = 1
    flag = True
    for count, *data in page:
        if count == 1:
            if data[1] == "R":
                if (data[0] <= curX):
                    flag = False
                    break
            else: curX = max(data[0] + 1, curX)
        
        else:
            if (data[1] == "R"): #선분
                if (curX < data[0]): continue
                elif (data[2] < curX): continue
                else: curX = max(data[2] + 1, curX)
            else:
                if (data[2] <= curX):
                    flag = False
                    break
                else: 
                    if (data[0] + 1 == data[2]):
                        flag = False
                        break
                    curX = max(data[0] + 1, curX)
                    
                
        
        if X < curX:
            flag = False
            break
    
    print(["NO", "YES"][flag])
    
    
if "__main__" == __name__: solve()