class Node:
    def __init__(self, data = None) -> None:
        self.data = data
        self.next = None
class singleList:
    def __init__(self) -> None:
        self.head = None

    def Append(self, new_data):
        new_node = Node(new_data)
        if self.head == None :
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
        return                    
    def Delete(self,key):
        current = self.head
        if current.data == key:
            self.head = current.next
            current = None
            return
        prev = current    
        while current:
            if current.data == key:
                prev.next = current.next
                current = None
                return
            prev = current
            current = current.next    

        return -1
    def displayList(self):
        temp = self.head
        while temp:
            print(temp.data,end="-->")
            temp = temp.next
        print("None")

if __name__ == "__main__":
    llist = singleList()
    llist.Append(5)
    llist.Append(4)
    llist.Append(3)
    llist.Append(9)
    llist.displayList()
    llist.Delete(5)
    llist.displayList()