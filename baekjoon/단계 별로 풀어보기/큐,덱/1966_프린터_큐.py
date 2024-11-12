import sys
input = sys.stdin.readline
IP = lambda: map(int, input().split())

def solve():
    for T in range(int(input())):
        N, M = IP()
        order = list(IP())
        find = order[M] = float(order[M])
        
        order.sort(reverse = True)
        print(order)
        
        
        print(order.index(find))
    
    
    
    
    
if "__main__" == __name__: solve()