
class Node:
    def __init__(self, data=None) -> None:
        self.data = data
        self.next = None


class CircularSingleList:
    def __init__(self) -> None:
        self.head = None
        self.tail = None

    def Append(self,new_data):
        new_node = Node(new_data)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
            new_node.next = self.head
        else:
            self.tail.next = new_node
            self.tail = new_node
            self.tail.next = self.head
            
    def DeleteNode(self,pos):
        current = self.head
        # Element at first position
        if pos == 1 :
            current = temp = self.head

            while current.next != self.head:
                current = current.next
            current.next = self.head.next
            self.head = self.head.next
            temp = None    
        else:
            current = self.head
            for i in range(0,pos-2): # 0-3
                current = current.next
            temp = current.next
            current.next = current.next.next
            temp = None    
        return

    def displayList(self):
        current = self.head
        if current == None:
            print("List is empty")
        else:
            print(current.data,end="-->")
            while current.next != self.head:
                current = current.next    
                print(current.data,end="-->")
        return   



if __name__ == "__main__":
    llist = CircularSingleList()
    llist.Append(10)       
    llist.Append(20)       
    llist.Append(50) 
    llist.Append(60) 
    llist.Append(70) 
    llist.displayList()
    llist.DeleteNode(5)
    print()
    llist.displayList()



