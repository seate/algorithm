input = __import__('sys').stdin.readline

def solve():
    w1, w2 = input().rstrip('\n'), input().rstrip('\n')
    X, Y = len(w1), len(w2)
    lcs = [[0] * (X + 1) for _ in range(Y + 1)]
    result_word = ""
    
    for y in range(1, Y + 1):
        for x in range(1, X + 1): lcs[y][x] = lcs[y - 1][x - 1] + 1 if w1[x - 1] == w2[y - 1] else max(lcs[y - 1][x], lcs[y][x - 1])
    
    while lcs[Y][X]:
        if lcs[Y - 1][X] == lcs[Y][X]: Y -= 1
        elif lcs[Y][X - 1] == lcs[Y][X]: X -= 1
        else: result_word += w1[X - 1]; Y -= 1; X -= 1
    
    print(lcs[-1][-1])
    print(''.join(result_word[::-1]))

if "__main__" == __name__: solve()