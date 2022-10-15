
class Node:
    def __init__(self, data = None) -> None:
        self.data = data
        self.next = None

class SingleList:
    def __init__(self) -> None:
        self.head = None
        self.tail = None
    def Append(self, new_data):
        new_node = Node(new_data)
        if self.head == None:
            self.head = new_node
            self.tail = self.head
            
        else:
            self.tail.next = new_node
            self.tail = self.tail.next

        return

    def reverseList(self):
        current = self.head
        temp = current.next
        current.next  = None
        while temp:
            prev = current
            current = temp
            temp = current.next
            current.next = prev
        self.head = current
        return    
                 

    def displayList(self):
        if self.head == None:
            print("List is None")
            return
        temp = self.head
        while temp:
            print(temp.data, end="-->")
            temp = temp.next
        print("None")
        return



if __name__ == "__main__":
    llist = SingleList()
    llist.Append(10)        
    llist.Append(30)        
    llist.Append(60)        
    llist.Append(70)        
    llist.Append(80)    


    llist.displayList()
    llist.reverseList()

    llist.displayList()    
