import sys
input = sys.stdin.readline
IP = lambda: map(int, sys.stdin.readline().split())

def solve():
    N, result = IP()
    person, start, end = [], -1, -1
    
    for i in range(N):
        a, b = IP()
        if b < a: person.append((b, a))
    person.sort()
    
    for p in person:
        if p[1] <= end: continue
        elif end < p[0]:
            result += (end - start) * 2
            start = p[0]
        end = p[1]
    
    print(result + (end - start) * 2)
    
if "__main__" == __name__: solve()