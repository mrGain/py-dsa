from collections import deque as Queue 

que = Queue()
# print(que)
que.append(2)
que.append(6)
que.append(5)
print(que)
print(que.popleft())

que.appendleft(9)
print(list(que))
que.clear()
print(que)