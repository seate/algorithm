input = __import__('sys').stdin.readline

def solve():
    N = int(input())
    roots = [None] * (N + 1); linked = [[] for _ in range(N + 1)]
    
    for _ in range(N - 1): a, b = map(int, input().split()); linked[a].append(b); linked[b].append(a)
    present = [1]
    while present:
        present_num = present.pop()
        for each in linked[present_num]:
            if roots[each] == None: roots[each] = present_num; present.append(each)
    print('\n'.join(map(str, roots[2:])))

if "__main__" == __name__: solve()