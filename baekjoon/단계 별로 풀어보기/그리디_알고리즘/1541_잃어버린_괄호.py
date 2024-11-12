import sys
input = sys.stdin.readline
IP = lambda: map(int, input().split())

def solve():
    formula = [i.split("+") for i in input().rstrip().split("-")]
    for i in formula:
        for j in i: j.lstrip("0")
    
    result = sum(map(int, formula[0]))
    for i in formula[1:]: result -= sum(map(int, i))
    
    print(result)
    
if "__main__" == __name__: solve()