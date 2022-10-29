class Queue:
    def __init__(self):
        self.que = []

    def __str__(self):
        values = [str(x) for x in self.que]  
        return ' '.join(values) 


    # Check wether the queue is empty
    def isEmpty(self):
        if self.que == []:
            return True
        else:
            return False
    def enQueue(self,item):
        self.que.append(item)
        return "The element is inserted in the Queue."

    def deQueue(self):
        if self.isEmpty():
            return "Queue Underflow"
        else:
            return self.que.pop(0)

    def peek(self):
        if self.isEmpty():
            return "Queue Underflow"
        else:
            return self.que[0]

    def delete(self):
        self.que = None            


que = Queue()
print(que.isEmpty())
que.enQueue(10)
que.enQueue(7)
que.enQueue(14)
que.enQueue(30)
print(que)
que.deQueue()
print(que)