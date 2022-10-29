# Created by Rakesh Gain 
# Copyright ©️ 2022 Auther.All right reserved.


class Queue:
    def __init__(self, maxSize):
        self.que = [None]*maxSize
        self.maxSize = maxSize
        self.front = -1
        self.rear = -1 

    def __str__(self):
        values = [str(x) for x in self.que]
        return ' '.join(values)

    # To check the Queue to be full 
    def isFull(self):
        if self.front == 0 and self.rear + 1 == self.maxSize:
            return True
        elif self.rear + 1 == self.front:
            return True
        else:
            return False 

    # To chceck wether the Queue is Empty 
    def isEmpty(self):
        if self.rear == -1 :
            return True 
        else:
            return False 

    def enQueue(self,data):
        if self.isFull():
            return "The Queue Overflow"
        else:
            if self.rear + 1 == self.maxSize:
                self.rear = 0
            else:
                self.rear += 1
                if self.front == -1:
                    self.front = 0
            self.que[self.rear] = data 
            return "Data inserted in the Queue" 


    def deQueue(self):
        if self.isEmpty():
            return "Queue Underflow"
        else:
            firstElement = self.que[self.front]
            front = self.front
            if self.front == self.rear:
                self.front = -1
                self.rear = -1
            elif self.front + 1 == self.maxSize:
                self.front = 0  
            else:
                self.front += 1

            self.que[front] = None 

            return firstElement
    
    def peek(self):
        if self.isEmpty():
            return "Queue underflow"
        else:
            return self.que[self.front]    

    def delete(self):
        self.que = [None] * self.maxSize
        self.front = -1
        self.rear = -1        

que = Queue(3)
# print(que.isFull())                      
# print(que.isEmpty())      

que.enQueue(1)                
que.enQueue(2)                
que.enQueue(3)     
print(que)        
que.deQueue()   
que.deQueue()   
print(que)    
que.enQueue(4)   
que.enQueue(4)   
print(que.enQueue(5))
print(que)    
print(que.peek())
