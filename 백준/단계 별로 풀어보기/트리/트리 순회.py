import sys
input = sys.stdin.readline

def solve():
    N = int(input())
    Tr = dict()
    
    for i in range(N):
        Node, *children = input().split()
        Tr[Node] = children
    
    preorder = []
    inorder = []
    postorder = []
    
    def traversal(present):
        preorder.append(present)
        if Tr[present][0] != '.': traversal(Tr[present][0])
        inorder.append(present)
        if Tr[present][1] != '.': traversal(Tr[present][1])
        postorder.append(present)
    
    traversal('A')
    
    print(''.join(preorder))
    print(''.join(inorder))
    print(''.join(postorder))

if "__main__" == __name__:
    solve()