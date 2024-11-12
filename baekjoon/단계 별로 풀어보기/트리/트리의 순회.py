input = __import__('sys').stdin.readline

def solve():
    N = int(input())
    inorder = input().split()
    postorder = input().split()
    
    result = []
    Stack = [((0, N), (0, N))]
    
    inorder_loacte = dict()
    for i in range(N): inorder_loacte[inorder[i]] = i
    
    while Stack:
        inorder_index, postorder_index = Stack.pop()
        
        inorder_start, inorder_end = inorder_index
        postorder_start, postorder_end = postorder_index
        
        root = postorder[postorder_end - 1]
        result.append(root)
        
        root_index_in_inorder = inorder_loacte[root]
        
        inorder_left_child_index = (inorder_start, root_index_in_inorder)
        inorder_right_child_index = (root_index_in_inorder + 1, inorder_end)
        
        inorder_left_child_length = root_index_in_inorder - inorder_start
        
        postorder_left_child_index = (postorder_start, postorder_start + inorder_left_child_length)
        postorder_right_child_index = (postorder_start + inorder_left_child_length, postorder_end - 1)
        
        if inorder_right_child_index[0] != inorder_right_child_index[1] and postorder_right_child_index[0] != postorder_right_child_index[1]:
            Stack.append((inorder_right_child_index, postorder_right_child_index))
        
        if inorder_left_child_index[0] != inorder_left_child_index[1] and postorder_left_child_index[0] != postorder_left_child_index[1]:
            Stack.append((inorder_left_child_index, postorder_left_child_index))
        
    print(' '.join(result))
    

if "__main__" == __name__: solve()