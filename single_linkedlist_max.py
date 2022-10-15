
class Node:
    def __init__(self,data=None) -> None:
        self.data = data
        self.next = None

class SingleList:
    def __init__(self) -> None:
        self.head = None 

    def Append(self,new_data):
        new_node = Node(new_data)

        if self.head == None:
            self.head = new_node
            return

        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node
        return
    
    def largestInList(self):
        max = -32767   # max variable initialized with INT_MIN value
        temp = self.head
        while temp:
            if temp.data > max:
                max = temp.data
            temp = temp.next    
        return max
    
    # method to find the smallest elemetn in a linedlist
    def smallestInList(self):
        min = 32767
        temp = self.head
        while temp:
            if temp.data < min:
                min = temp.data
            temp = temp.next
        return min

    def displayList(self):
        temp = self.head
        while temp:
            print(temp.data, end="-->")
            temp = temp.next
        print("None")
        return    

if __name__ == "__main__":
    llist = SingleList()
    llist.Append(10)
    llist.Append(4)
    llist.Append(5)
    llist.Append(2)
    llist.Append(15)
    llist.displayList()
    max = llist.largestInList()
    print("Maximum in the list",max)

    min = llist.smallestInList()
    print("smallest in the list",min)






