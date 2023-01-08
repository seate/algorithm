import sys

def bottom_up_sort(the_heap):
    present_index = len(the_heap) - 1
    
    while True:
        next_index = present_index // 2
        
        if abs(the_heap[present_index]) < abs(the_heap[next_index]) or (abs(the_heap[present_index]) == abs(the_heap[next_index]) and the_heap[present_index] < the_heap[next_index]):
            the_heap[present_index], the_heap[next_index] = the_heap[next_index], the_heap[present_index]
            present_index = next_index
        else: break


def top_down_sort(the_heap):
    present_index = 1
    last_index = len(the_heap) - 1
    
    while True:
        next_index = present_index * 2
        
        if next_index + 1 <= last_index:
            next_index += 0 if (abs(the_heap[next_index]) < abs(the_heap[next_index + 1])) or (abs(the_heap[next_index]) == abs(the_heap[next_index + 1]) and the_heap[next_index] < the_heap[next_index + 1]) else 1
            
            if abs(the_heap[present_index]) > abs(the_heap[next_index]) or (abs(the_heap[present_index]) == abs(the_heap[next_index]) and the_heap[present_index] > the_heap[next_index]):
                the_heap[present_index], the_heap[next_index] = the_heap[next_index], the_heap[present_index]
                present_index = next_index
            else: break
        
        elif next_index == last_index:
            if (abs(the_heap[present_index]) > abs(the_heap[next_index])) or (abs(the_heap[present_index]) == abs(the_heap[next_index]) and the_heap[present_index] > the_heap[next_index]):
                the_heap[present_index], the_heap[next_index] = the_heap[next_index], the_heap[present_index]
                present_index = next_index
            break
        
        else: break


heap = [0]
for i in range(int(sys.stdin.readline())):
    command = int(sys.stdin.readline())
    
    if command == 0:
        if len(heap) == 1: print(0)
        elif len(heap) == 2: print(heap.pop())
        else:
            print(heap[1])
            heap[1] = heap.pop()
            top_down_sort(heap)
    
    else:
        heap.append(command)
        bottom_up_sort(heap)