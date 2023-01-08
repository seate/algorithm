import bisect
input = __import__('sys').stdin.readline

def LIS():
    input()
    arr = list(map(int, input().split()))
    
    lis_arr = [arr[0]]
    res = [1]
    for n in arr[1:]:
        if lis_arr[-1] < n:
            lis_arr.append(n)
            res.append(len(lis_arr))
        else:
            where = bisect.bisect_left(lis_arr, n)
            lis_arr[where] = n
            res.append(where + 1)
    
    i = len(lis_arr)
    print(i)
    ans = []
    for idx in range(len(res) - 1, -1, -1):
        if res[idx] == i:
            ans.append(arr[idx])
            i -= 1
    print(' '.join(map(str, ans[::-1])))

if "__main__" == __name__: LIS()