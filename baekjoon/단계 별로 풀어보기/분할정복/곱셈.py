def mul(a, b):
    if b == 0: return 1
    elif b == 1: return a
    elif b % 2 == 1: return mul(a, b - 1) * a
    else: return (mul(a, b // 2) % c) ** 2 % c
a, b, c = map(int, input().split())
print(mul(a,b) % c)