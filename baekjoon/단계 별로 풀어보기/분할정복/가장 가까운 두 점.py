import sys
input = sys.stdin.readline

#두 점을 거리를 구해서 return
def dist(x1, x2): return (x1[0] - x2[0]) ** 2 + (x1[1] - x2[1]) ** 2


def solve(coords, N):
    #기저사례
    #분할 했을 때 남은 것이 2개인 경우 2개를 비교해서 최소를 return함
    if N == 2: return dist(coords[0], coords[1])
    #분할 했을 때 남은 것이 3개인 경우 3개를 비교해서 최소를 return함
    elif N == 3: return min(dist(coords[0], coords[1]), dist(coords[0], coords[2]), dist(coords[1], coords[2]))
    
    
    #이분 탐색하는 명령어
    d = min(solve(coords[:N // 2], N // 2), solve(coords[N // 2:], N // 2))
    #x값의 중간을 mid에 저장함
    mid = (coords[N // 2][0] + coords[N // 2 - 1][0]) // 2
    
    #x= mid 인 기준선을 기준으로 x축 좌표가 d 이상 떨어져 있는 점들을 제외한 list를 short_check에 저장함
    short_check = []
    for subset in coords:
        if (mid - subset[0]) ** 2 <= d: short_check.append(subset)
    #거르고 남은 점들을 y좌표 기준으로 정렬함
    short_check.sort(key = lambda x: x[1])
    
    #남은 점이 1개 뿐일 경우에는 답을 구했으므로 d를 return함
    if len(short_check) == 1: return d
    #
    else:
        y_check = d
        #y축 기준으로 거르기
        for i in range(len(short_check) - 1):
            for j in range(i + 1, len(short_check)):
                #기본적으로 거리가 d보다 먼 경우
                if (short_check[i][1] - short_check[j][1]) ** 2 > d: break
                #점이 둘 다 x = mid를 기준으로 왼쪽에 속하는 경우
                elif short_check[i][0] < mid and short_check[j][0] < mid: continue
                #점이 둘 다 x = mid를 기준으로 오른쪽에 속하는 경우
                elif short_check[i][0] > mid and short_check[j][0] > mid: continue
                
                y_check = min(y_check, dist(short_check[i], short_check[j]))
    
    return y_check



N = int(input())
coords = [list(map(int, input().split())) for i in range(N)]
coords_set = list(set(map(tuple, coords)))

if len(coords) != len(coords_set): print("0")
else:
    coords_set.sort()
    print(solve(coords_set, N))
