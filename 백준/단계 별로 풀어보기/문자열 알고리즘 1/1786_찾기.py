from sys import stdin

def solve():
    T = stdin.readline().rstrip('\n')
    P = stdin.readline().rstrip('\n')
    T_length = len(T); P_length = len(P)
    
    LPS = [0] * P_length
    length = 0; count = 0
    found_locate = []; i =1
    
    while i < P_length:
        if P[i] == P[length]:
            length += 1
            LPS[i] = length
            i += 1
        else:
            if length: length = LPS[length - 1]
            else: LPS[i] = 0; i += 1
    
    t_index = 0; p_index = 0
    while t_index < T_length:
        if T[t_index] == P[p_index]:
            t_index += 1
            p_index += 1
        else:
            if p_index: p_index = LPS[p_index - 1]
            else: t_index += 1
        
        if p_index == P_length:
            found_locate.append(t_index - p_index + 1)
            p_index = LPS[p_index - 1]
    
    print(len(found_locate))
    print(' '.join(map(str, found_locate)))
    
if "__main__" == __name__: solve()