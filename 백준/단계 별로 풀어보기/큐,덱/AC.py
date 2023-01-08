from collections import deque

for i in range(int(input())):
    command = input()
    length = int(input())
    value = deque(input().lstrip("[").rstrip("]").split(","))
    reverse = 1
    
    if length < command.count("D"):
        print("error")
        continue
    
    for j in command:
        if j == "R": reverse *= -1
        elif j == "D":
            if reverse == 1: value.popleft()
            elif reverse == - 1: value.pop()
    
    if command.count("R") % 2 != 0: value.reverse()
    
    print("[", end = '')
    for j in range(len(value)):
        if j == len(value) - 1: print(value[j], end = '')
        else: print(value[j], end = ',')
    print("]")