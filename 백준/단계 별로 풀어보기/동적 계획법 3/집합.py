import sys
input = sys.stdin.readline

S = set()
initialize_set = {i + 1 for i in range(20)}

for i in range(int(input())):
    command = input().split()
    if len(command) >= 2: command[1] = int(command[1])
    
    if command[0] == 'add': S.add(command[1])
    elif command[0] == 'remove': S.discard(command[1])
    elif command[0] == 'check': print(int(command[1] in S))
    elif command[0] == 'toggle':
        if command[1] in S: S.remove(command[1])
        else: S.add(command[1])
    elif command[0] == 'all': S = initialize_set
    elif command[0] == 'empty': S = set()