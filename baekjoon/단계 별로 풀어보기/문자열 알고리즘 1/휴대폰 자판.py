import sys
input = sys.stdin.readline
IP = lambda: map(int, sys.stdin.readline().split())
sys.setrecursionlimit(10 ** 9)

def my_solve():
    class Node(object):
        def __init__(self):
            self.children = dict()
            self.terminal = False
    
    def dfs(present, need_counter):
        if present.terminal:
            global result
            result += need_counter
        if present.terminal or 1 < len(present.children): need_counter += 1
        for child_letter in present.children: dfs(present.children[child_letter], need_counter)
    
    while True:
        global result
        start = Node(); result = 0
        try: N = int(input())
        except: break
        for i in range(N):
            present = start
            for letter in input().rstrip():
                if not letter in present.children:
                    present.children[letter] = Node()
                present = present.children[letter]
            present.terminal = True
            
        for initial in start.children: dfs(start.children[initial], 1)
        print("%.2lf" % round(result / N, 2))

def better_solve(): #half_time
    def dfs(present, counter):
        if len(present) == 1 and not '*' in present:
            for next_letter in present: dfs(present[next_letter], counter)
        else:
            for next_letter in present:
                if next_letter == '*': result[0] += counter
                else: dfs(present[next_letter], counter + 1)
    
    while True:
        try: N = int(input())
        except: break
        
        start = {}; result = [0] #result를 리스트 형식으로 하면 재귀함수에서 global을 선언하지 않아도 됨.
        for i in range(N):
            word = input().rstrip()
            present = start
            for letter in word:
                if not letter in present: present[letter] = {}
                present = present[letter]
            present['*'] = {}
        
        for first_letter in start: dfs(start[first_letter], 1)
        print("%.2lf" % round(result[0] / N, 2))

if "__main__" == __name__: better_solve()