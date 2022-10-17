

class Node:
    def __init__(self,data= None):
        self.data = data
        self.next = None

class SingleList:
    def __init__(self):
        self.head = None
        self.tail = None

    def Append(self, new_data):
        new_node = Node(new_data)
        if self.head == None: # checking if the list is none
            self.head = new_node
            self.tail = new_node
            new_node.next = self.head
        else:
             self.tail.next = new_node
             self.tail = new_node
             self.tail.next = self.head   
        return

    def insert(self,index,data):
        new_node = Node(data)
        if index<1:
            print("Invalid position")
        elif index == 1:
            current = self.head
            while current.next != self.head:
                current = current.next
            current.next = new_node
            new_node.next = self.head
            self.head = new_node
        else:        
            current = self.head
            for i in range(1,index-1):
                current = current.next
            new_node.next = current.next   
            current.next = new_node 
        return    
          
    def displayList(self):
        current = self.head
        if self.head == None:
            print("List is empty")
        else:
            print(current.data,end="-->")
            while current.next != self.head:
                current = current.next
                print(current.data,end="-->")    
        return    


if __name__ == "__main__":
    llist = SingleList()
    llist.Append(10)
    llist.Append(20)
    llist.Append(30)
    llist.displayList()
    # llist.insert(3,50)
    # llist.insert(4,23)
    llist.insert(1,8)
    print()
    llist.displayList()