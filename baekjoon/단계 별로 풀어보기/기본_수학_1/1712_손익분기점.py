def solve():
    a, b, c = map(int, __import__('sys').stdin.readline().split())
    print('-1' if c <= b else int(a / (c - b) + 1))
    
if "__main__" == __name__: solve()