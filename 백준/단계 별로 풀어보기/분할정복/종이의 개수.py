import math

spliter = 3


def box_cutting(box_list):
    #끝났을 경우
    if len(box_list[0]) == 1:
        counter[box_list[0][0]] += 1
        return
    
    #선언부
    box_length = len(box_list[0])
    next_box_list = []
    next_box_length = box_length // spliter
    first_number = None

    
    #일치 검사
    for i in range(box_length):
        for j in range(box_length):
            if first_number == None: first_number = box_list[0][0]
            #불일치의 경우
            elif first_number != box_list[i][j]:
                #다음으로 넘기기 위한 next_box_list 생성
                for k in range(spliter):
                    for l in range(spliter):
                        temp = []
                        for m in range(next_box_length): temp.append(box_list[k * next_box_length : (k + 1) * next_box_length][m][l * next_box_length : (l + 1) * next_box_length])
                        next_box_list.append(temp)
                for n in next_box_list: box_cutting(n)
                return
    #일치했을 경우
    counter[first_number] += 1


N = int(input())
temp_value = [list(map(int, input().split())) for i in range(N)]
temp_next = [[None for j in range(spliter)] for i in range(spliter)]
counter = [0, 0, 0]
box_cutting(temp_value)

for i in range(-1, 2): print(counter[i])