from sys import stdin
input = stdin.readline
IP = lambda: map(int, input().split())

def two_pointer_solve():
    start, end = 0, int(input()) - 1
    data = sorted(IP())
    result = float("inf"); result_element = None
    
    while start < end:
        present = data[start] + data[end]
        if abs(present) < result:
            result = abs(present)
            result_element = [data[start], data[end]]
        
        if present <= 0: start += 1
        else: end -= 1
    
    print(' '.join(map(str, result_element)))

def fast_solve():
    input(); data = sorted(IP(), key = lambda x: abs(x))
    result = 2 * 10 ** 10; result_element = None; previous = data[0]
    
    for present in data[1:]:
        if abs(previous + present) < result:
            result = abs(previous + present)
            result_element = [previous, present]
        previous = present
    
    print(' '.join(map(str, sorted(result_element))))

if "__main__" == __name__:
    #two_pointer_solve()
    fast_solve()