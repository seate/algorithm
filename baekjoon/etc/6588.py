isPrime = [True] * 1000010

for i in range(2, 1000010):
    if not isPrime[i]: continue
    
    while cur < len(isPrime):
        cur += i
        isPrime[cur] = False

    
L = [i for i in range(3, len(isPrime)) if isPrime[i] and (i % 2)]
s = set(L)

while True:
    num = int(input())
    if num == 0: break
    
    for cur in L:
        if (num - cur) in s:
            print(num, "=", cur, "+", num - cur)
            break