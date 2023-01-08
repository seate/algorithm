import sys
input = sys.stdin.readline
IP = lambda: map(int, sys.stdin.readline().split())

def solve():
    for T in range(int(input())):
        N, *data = IP()
        average = sum(data) / N
        counter = 0
        for each in data:
            if average < each: counter += 1
        
        print("%.3lf" % round(counter / N * 100, 3) + "%")
    
if "__main__" == __name__: solve()