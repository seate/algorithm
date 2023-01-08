import math

def quad(box_list, index = 0):
    box_length = len(box_list[0])
    hf = box_length // 2
    first_check = 2
    four_box = [[] for i in range(4)]
    for i in box_list[:hf]:
        four_box[0].append(i[:hf])
        four_box[1].append(i[hf:])
    for i in box_list[hf:]:
        four_box[2].append(i[:hf])
        four_box[3].append(i[hf:])
    for i in range(box_length):
        for j in range(box_length):
            if first_check == 2: first_check = box_list[0][0]
            else:
                if first_check != box_list[i][j]:
                    result.append("(")
                    for k in range(4): quad(four_box[k], index + 1)
                    result.append(")")
                    return
    result.append(first_check)

N = int(input())
value = []
for i in range(N):
    temp = input()
    temp2 = []
    for j in temp: temp2.append(j)
    value.append(temp2)

k = int(math.log(N, 2))
result = []
quad(value)
for i in result: print(i, end = '')