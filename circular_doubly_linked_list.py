class Node:
    def __init__(self,data=None):
        self.data = data 
        self.prev = None
        self.next = None

class CircularDoublyList:
    def __init__(self):
        self.head = None 
        self.tail = None 

    def Insert(self,new_data,position=None):
        new_node = Node(new_data)
        # If position is None
        if self.head == None and position == None :
            self.head = new_node
            self.tail = new_node 
            new_node.next = self.head
            return 

        else:
            if position == None:
                self.tail.next = new_node
                new_node.next = self.head
                self.tail = new_node

            return

    def displayList(self):
        if self.head == None:
            print("List not exists")
            return

        temp = self.head
        print(temp.data,end="-->")
        while temp.next != self.head:
            temp = temp.next 
            print(temp.data,end="-->")
        #print(self.head, temp.next)    
        return

cdll = CircularDoublyList()
cdll.Insert(20)     
cdll.Insert(30)     
cdll.Insert(40)     
cdll.Insert(4)     
cdll.Insert(12)     
cdll.displayList()          