def mul(a, b, c):
    if b <= 1: return a ** b
    elif b % 2 == 1: return mul(a, b - 1, c) * a
    else: return (mul(a, b // 2, c) % c) ** 2 % c

n_pack, k_packs, p = 1, 1, 1000000007
N, K = map(int, input().split())

for i in range(1, N + 1):
    n_pack *= i
    n_pack %= p
for i in range(1, K + 1):
    k_packs *= i
    k_packs %= p
for i in range(1, N - K + 1):
    k_packs *= i
    k_packs %= p
print((n_pack * mul(k_packs, p - 2, p)) % p)