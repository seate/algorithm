import sys
import collections
sys.setrecursionlimit(10 ** 6 + 5)
input = sys.stdin.readline

def Tree_making():
    values = []
    while True:
        try: values.append(int(input()))
        except: break
    
    preorder = [values]
    
    Tree = dict()
    sub_trees = collections.deque(preorder)
    
    while sub_trees:
        each_tree = sub_trees.popleft()
        root = each_tree[0]
        
        each_tree.append(float("inf"))
        for idx in range(1, len(each_tree)):
            if root < each_tree[idx]: break
        each_tree.pop()
        
        Tree[root] = [None, None]
        if len(each_tree[1:idx]):
            sub_trees.append(each_tree[1:idx])
            Tree[root][0] = each_tree[1]
        if len(each_tree[idx:]):
            sub_trees.append(each_tree[idx:])
            Tree[root][1] = each_tree[idx]
    
    postorder = []
    def Postorder(present):
        if Tree[present][0] != None: Postorder(Tree[present][0])
        if Tree[present][1] != None: Postorder(Tree[present][1])
        postorder.append(present)
    
    Postorder(preorder[0][0])
    
    print('\n'.join(map(str, postorder)))

def non_Tree_making():
    preorder = []
    while True:
        try: preorder.append(int(input()))
        except: break
    
    def postorder(start, end):
        if start > end: return
        
        divide_point = end + 1
        for idx in range(start + 1, end + 1):
            if preorder[start] < preorder[idx]: divide_point = idx; break
        
        postorder(start + 1, divide_point - 1)
        postorder(divide_point, end)
        print(preorder[start])
    
    postorder(0, len(preorder) - 1)


def best_solve():
    #ret = 넘어가야 할 부분 지정?
    def dfs(pos, min_v):
        ret = 0
        
        #1같은 집합내에서 진행?
        if pos + 1 < len(orders) and orders[pos] > orders[pos + 1]:
            ret += dfs(pos + 1, min(min_v, orders[pos]))
        
        #2오른쯕으로 넘어가기?
        if pos + ret + 1 < len(orders) and orders[pos] < orders[pos + ret + 1] and orders[pos + ret + 1] < min_v:
            ret += dfs(pos + ret + 1, min_v)
        
        print(orders[pos])
        return ret + 1
    
    orders = []
    for v in map(int, sys.stdin.read().split()): orders.append(v)
    dfs(0, 0x3c3c3c3c)
    

if "__main__" == __name__:
    #Tree_making()
    #non_Tree_making()
    best_solve()