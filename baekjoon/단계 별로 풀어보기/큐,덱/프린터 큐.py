from collections import deque

for i in range(int(input())):
    n, m = map(int, input().split())
    documents = deque(map(int, input().split()))
    documents[m] = float(documents[m])
    seq = 1
    
    while True:
        if documents[0] == max(documents):
            if type(documents[0]) == float:
                print(seq)
                break
            else:
                seq += 1
                documents.popleft()
        else: documents.append(documents.popleft())