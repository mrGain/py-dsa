from collections import deque as Queue 

que = Queue(maxlen=5)
# print(que)
que.append(2)
que.append(6)
que.append(5)
print(que)
print(que.popleft())

que.appendleft(9)
print(list(que),str(que.maxlen))
que.clear()
print(que)