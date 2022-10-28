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


    def queFront(self):
        if self.isEmpty():
            print("Sorry the Queue is Empty.")

que = Queue()
print(que.isEmpty())
que.enQueue(10)
que.enQueue(7)
que.enQueue(14)
que.enQueue(30)
print(que)