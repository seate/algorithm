import sys
input = sys.stdin.readline

def solve():
    Q = [int(input()) for T in range(int(input()))]
    
    end = max(Q) + 1
    save = [True] * (end // 2)
    for i in range(3, int(end ** 0.5) + 1, 2):
        if save[i // 2]:
            k = i * i
            save[k // 2 :: i] = [False] * ((end - k - 1) // (2 * i) + 1)
    primes = {2 * i + 1 for i in range(1, end // 2) if save[i]}
    
    result = ""
    for each in Q:
        if each == 4: result += '2 2\n'; continue
        half = each // 2
        for i in range(not half & 1, half, 2):
            if half + i in primes and half - i in primes: result += f"{half - i} {half + i}\n"; break
    
    print(result)
    
if "__main__" == __name__: solve()