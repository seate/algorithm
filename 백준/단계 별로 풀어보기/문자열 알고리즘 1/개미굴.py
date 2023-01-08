import sys
input = sys.stdin.readline

def solve():
    def dfs(present_index = 0, depth = 0):
        for child_name in sorted(dict_list[present_index]):
            print('--' * depth, child_name, sep = '')
            dfs(dict_list[present_index][child_name], depth + 1)
    
    dict_list = [dict()]; dict_list_length = 1
    
    for n in range(int(input())):
        length, *trace = input().split()
        dict_index = 0
        for i in range(int(length)):
            if trace[i] in dict_list[dict_index]: dict_index = dict_list[dict_index][trace[i]]
            else:
                dict_list.append(dict())
                dict_list[dict_index][trace[i]] = dict_list_length
                dict_index = dict_list_length
                dict_list_length += 1
    
    dfs()
    
if "__main__" == __name__: solve()