def BFS(present_list):
    list_for_next, idx = [], 0
    
    while True:
        
        next_locate = []
        
        for i in present_list:
            if i == destination: return idx
            
            
            if i > 0 and visitable[i - 1]:
                next_locate.append(i - 1)
                visitable[i - 1] = False
            
            if destination > i:
                if i <= 50000 and visitable[i * 2]:
                    next_locate.append(i * 2)
                    visitable[i * 2] = False
                    
                if i < 100000 and visitable[i + 1]:
                    next_locate.append(i + 1)
                    visitable[i + 1] = False
        
        present_list = next_locate[:]
        idx += 1

present, destination = map(int, input().split())
visitable = [True] * (100010)
visitable[present] = False
print(BFS([present]))