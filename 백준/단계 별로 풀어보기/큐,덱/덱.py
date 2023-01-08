from collections import deque
import sys

deq = deque()

for i in range(int(sys.stdin.readline())):
    command = sys.stdin.readline().split()
    cmd = command[0]
    
    if cmd == "push_front": deq.appendleft(int(command[1]))
    elif cmd == "push_back": deq.append(int(command[1]))
    elif cmd == "size": print(len(deq))
    elif cmd == "empty": print({True: "0", False: "1"}.get(bool(deq
    )))
    elif len(deq) >= 1:
        if cmd == "pop_front": print(deq.popleft())
        elif cmd == "pop_back": print(deq.pop())
        elif cmd == "front": print(deq[0])
        elif cmd == "back": print(deq[-1])
    else: print("-1")