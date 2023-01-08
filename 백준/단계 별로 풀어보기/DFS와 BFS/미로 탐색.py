import sys
sys.setrecursionlimit(10 ** 8)

def BFS(present_list, present_index = 1):
    list_for_next = []
    
    for y, x in present_list:
        if y != 0 and visitable[y - 1][x]:
            list_for_next.append([y - 1, x])
            visitable[y - 1][x] = False
        
        if y != N - 1 and visitable[y + 1][x]:
            list_for_next.append([y + 1, x])
            visitable[y + 1][x] = False
        
        if x != 0 and visitable[y][x - 1]:
            list_for_next.append([y , x - 1])
            visitable[y][x - 1] = False
        
        if x != M - 1 and visitable[y][x + 1]:
            list_for_next.append([y, x + 1])
            visitable[y][x + 1] = False
    
    if [N - 1, M - 1] in list_for_next: return present_index + 1
    return BFS(list_for_next, present_index + 1)

N, M = map(int, input().split())
visitable = [list(map(bool, map(int, list(input())))) for i in range(N)]
print(BFS([[0, 0]]))