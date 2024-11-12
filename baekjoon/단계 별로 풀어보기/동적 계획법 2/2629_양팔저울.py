import sys
input = sys.stdin.readline
IP = lambda: map(int, input().split())

def solve():
    weight_count = int(input())
    weight = list(IP())
    marble_count = int(input())
    marble = list(IP())
    checkable = set([0])
    
    for w in weight:
        temp_set = set()
        for i in checkable:
            if w < i: temp_set.add(i - w)
            if i < w: temp_set.add(w - i)
            temp_set.add(i + w)
        checkable.update(temp_set)
    
    print(' '.join(['Y' if m in checkable else 'N' for m in marble]))

if "__main__" == __name__: solve()