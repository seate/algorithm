K, N = map(int, input().split())
value = [int(input()) for i in range(K)]
present_cutter = max(value)
jumper = present_cutter // 2 if present_cutter != 1 else 1
exceed, exact, lack = 0, 0, 0
line_counter = sum([i // present_cutter for i in value])

while True:
    if line_counter < N: present_cutter -= jumper
    elif N <= line_counter: present_cutter += jumper
    jumper = jumper // 2 if jumper % 2 != 1 else jumper // 2 + 1
    if present_cutter == 0: present_cutter = 1
    line_counter = sum([i // present_cutter for i in value])
    
    if jumper == 1:
        if not lack and line_counter < N: lack = max(exceed, exact, lack) + 1
        elif not exceed and N < line_counter: exceed = max(exceed, exact, lack) + 1
        elif not exact and N == line_counter: exact = max(exceed, exact, lack) + 1
        
        if lack == 1 and (exact or exceed): break
        elif lack >= 2:
            present_cutter -= 1
            break
print(present_cutter)