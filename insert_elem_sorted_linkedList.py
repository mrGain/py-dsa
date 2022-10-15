
class Node:
    def __init__(self, data=None) -> None:
        self.data = data
        self.next = None

class SingleList:
    def __init__(self) -> None:
        self.head = None

    def Append(self, new_data):
        new_node = Node(new_data)
        if self.head == None:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next

        temp.next = new_node
        return
    # method to insert the element to shorted List 
    def insertSortedPosition(self, data):
        new_node = Node(data)
        current = self.head
        prev = self.head
        # If the first element is grater than entered element
        # then entered element should be the first element
        if current.data >= data:
            new_node.next = current
            self.head = new_node
            return
        while current:
            if current.data >= data:
                temp = prev.next
                prev.next = new_node
                new_node.next = temp
                return
            prev = current
            current = current.next  
              
        self.Append(data)
        return       


    def displayList(self):
        current = self.head
        while current:
            print(current.data, end="-->")
            current = current.next
        print("None")
        return

if __name__ == "__main__":
    llist = SingleList()
    arr = [4,7,12,15,20,33]
    for i in arr:
        llist.Append(i)
    llist.displayList()                
    llist.insertSortedPosition(34)
    llist.displayList()                