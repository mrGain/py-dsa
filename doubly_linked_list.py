
class Node:
    def __init__(self, data = None):
        self.data = data
        self.prev = None 
        self.next = None

class DoublyList:  
    def __init__(self):
        self.head = None
        self.tail = None
        
    def Append(self, new_data):
        new_node = Node(new_data)
        
        # For Empty List
        if self.head == None:
            self.head = new_node
            self.tail = new_node
            return 
        else:
            prev = self.tail
            self.tail.next = new_node
            new_node.prev = prev
            self.tail = new_node
        return  

    # Printing the list in reverse
    def reversePrint(self):
        temp = self.tail
        while temp:
            print(temp.data,end="-->")
            temp = temp.prev
        return    

    def diplayList(self):
        temp = self.head
        while temp:
            print(temp.data,end="-->")
            temp = temp.next
        return

dll = DoublyList()
dll.Append(10)            
dll.Append(20)            
dll.Append(30)

dll.diplayList()
print()
dll.reversePrint()
