import sys
sys.setrecursionlimit(10000)

def moving(present_x = 0, present_y = 0):
    if method_box[present_y][present_x] == None:
        method_box[present_y][present_x] = 0
        if present_y != 0 and heights[present_y - 1][present_x] < heights[present_y][present_x]: method_box[present_y][present_x] += moving(present_x, present_y - 1)
        if present_x != N - 1 and heights[present_y][present_x + 1] < heights[present_y][present_x]: method_box[present_y][present_x] += moving(present_x + 1, present_y)
        if present_y != M - 1 and heights[present_y + 1][present_x] < heights[present_y][present_x]: method_box[present_y][present_x] += moving(present_x, present_y + 1)
        if present_x != 0 and heights[present_y][present_x - 1] < heights[present_y][present_x]: method_box[present_y][present_x] += moving(present_x - 1, present_y)
    return method_box[present_y][present_x]

M, N = map(int, input().split())
heights = [list(map(int, input().split())) for i in range(M)]
method_box = [[None for i in range(N)] for j in range(M)]
method_box[-1][-1] = 1
moving()
print(method_box[0][0])