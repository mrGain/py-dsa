import queue as q 

que = q.Queue(maxsize=3)

# To check wether the Que is Empty
print(que.empty())

# To insert the data inside the Queue
que.put(3)
que.put(4)
que.put(5)
# To check the que size
print(que.qsize())

# To check wether the que is full 
print(que.full())

# To Deque a data from the queue 
print(que.get())

print(que.qsize())

# To print all the elemnt inside the que
for n in que.queue:
    print(n,end=" ")
