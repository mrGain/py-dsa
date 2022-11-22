


class Node:
    def __init__(self, data = None):
        self.data = data 
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None 

class Queue:
    def __init__(self):
        self.llist = LinkedList()

    def isEmpty(self):
        if self.llist.head == None:
            return True
        else:
            return False

    def enQueue(self, data):
        node = Node(data)
        if self.llist.head == None:
            self.llist.head = node
            self.llist.tail = node
            return 
        else:
            self.llist.tail.next = node
            self.llist.tail = node     

    def deQueue(self):
        if self.isEmpty():
            return "Queue Underflow"
        else:
            tempNode = self.llist.head.data
            if self.llist.head == self.llist.tail:
                self.llist.head = None
                self.llist.tail = None

            else:
                self.llist.head = self.llist.head.next   
            return tempNode
    def peek(self):
        if self.isEmpty():
            return "Queue Underflow"
        else:
            return self.llist.head.data
            
    def printList(self):
        temp = self.llist.head
        while temp:
            print(temp.data, end="-->")
            temp = temp.next 
        print("None")
        return    

    def delete(self):
        self.llist.head = None
        self.llist.tail = None
        return
"""
que = Queue()
que.enQueue(3)
que.enQueue(5)
que.enQueue(8)
que.enQueue(12)
que.enQueue(34)
que.enQueue(10)

que.printList()
print(que.deQueue())
print(que.deQueue())
print(que.deQueue())
que.printList()
"""