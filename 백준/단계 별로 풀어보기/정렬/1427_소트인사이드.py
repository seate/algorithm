import sys
input = sys.stdin.readline
IP = lambda: map(int, input().split())

def solve():
    N = input().rstrip()
    counter = [0] * 11
    for letter in N: counter[int(letter)] += 1
    print(''.join([f"{i}" * counter[i] for i in range(10, -1, -1)]))
    
if "__main__" == __name__: solve()