import sys
input = sys.stdin.readline
IP = lambda: map(int, input().split())

def solve():
    N = int(input())
    distances = list(IP())
    prices = list(IP())
    #if N == 2: print(distances[0] * prices[0]); return #시간 단축용..
    answer = 0
    min_price = prices[0]
    
    for i in range(N - 1):
        if prices[i] < min_price: min_price = prices[i]
        answer += (distances[i] * min_price)
    
    print(answer)

if "__main__" == __name__: solve()