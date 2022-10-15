

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

    def checkIfSorted(self):
        current = prev = self.head
        while current:
            if current.data < prev.data:
                return -1
            prev = current
            current = current.next    
        return True
    def displayList(self):
        temp = self.head
        while temp:
            print(temp.data, end="-->")
            temp = temp.next
        print("None")

        return


if __name__ == "__main__":
    llist = SingleList()
    llist.Append(1)
    llist.Append(4)
    llist.Append(13)
    llist.Append(3)
    llist.Append(32)
    llist.displayList()
    print(llist.checkIfSorted())

         
