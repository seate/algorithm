import sys
from math import log2
from collections import deque, defaultdict
input = sys.stdin.readline
IP = lambda: map(int, input().split())
sys.setrecursionlimit(10 ** 9)

def solve():
    N = int(input())
    logN = int(log2(N)) + 1
    edge = [[] for _ in range(N + 1)]
    depth = [0] * (N + 1)
    DP = [[-1] * logN for i in range(N + 1)]; DP[1][0] = 0
    q = deque([1])
    
    
    for _ in range(N - 1):
        a, b = IP()
        edge[a] += [b]; edge[b] += [a]
    
    while q:
        present = q.popleft()
        for i in edge[present]:
            if DP[i][0] == -1:
                q.append(i)
                DP[i][0] = present
                depth[i] = depth[present] + 1
    
    for j in range(1, logN):
        for i in range(1, N + 1):
            DP[i][j] = DP[DP[i][j - 1]][j - 1]
    
    for _ in range(int(input())):
        a, b = IP()
        if depth[b] < depth[a]: a, b = b, a
        differ = depth[b] - depth[a]
        
        for i in range(logN):
            if differ & (1 << i): b = DP[b][i]
        
        if a == b:
            print(a)
            continue
        
        for i in range(logN - 1, -1, -1):
            if DP[a][i] != DP[b][i]: a = DP[a][i]; b = DP[b][i]
        
        print(DP[b][0])

def union_solve():
    def find_parent(search):
        if parent[search] == search: return search
        parent[search] = find_parent(parent[search])
        return parent[search]
    
    def dfs(present):
        parent[present] = present
        
        for next_node in edge[present]:
            if next_node in parent: continue
            dfs(next_node)
            parent[find_parent(next_node)] = present #이 줄 자체는 그저 부모 노드 저장하기임
        
        finished[present] = True
        
        for other_element in querys[present]: #해당하는 쿼리가 있으면 최소 공통 조상까지 유니온을 행하면서 올라감 -> 결과적으로 시간 단축?
            if finished[other_element]: answer[(present * maxN + other_element if present < other_element else other_element * maxN + present)] = find_parent(other_element)
    
    N = int(input())
    maxN = 1 << 17 #최댓값인 10만 초과 -> 앞 수와 뒷 수 구분
    edge = [[] for i in range(N + 1)]
    for i in range(N - 1):
        a, b = IP()
        edge[a].append(b); edge[b].append(a)
    
    querys = defaultdict(list)
    answer_order = [] #출력 순서 저장
    for i in range(int(input())):
        a, b = IP()
        querys[a].append(b); querys[b].append(a)
        answer_order.append((a * maxN + b if a < b else b * maxN + a)) # 작은 수 * 구분 수 + 큰 수
    
    parent = dict()
    answer = dict()
    finished = [False] * (N + 1) #이 노드 밑의 서브트리에서 방문이 끝나고 이 노드에서 리턴 되면 True
    
    dfs(1)
    print('\n'.join(map(str, [answer[i] for i in answer_order])))

if "__main__" == __name__:
    #solve()
    union_solve()