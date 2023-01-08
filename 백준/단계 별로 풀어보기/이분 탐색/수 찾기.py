n = int(input())
n_value = list(map(int,input().split()))
m = int(input())
m_value = list(map(int,input().split()))
for it in m_value:
    if it in n_value: print("1")
    else: print("0")