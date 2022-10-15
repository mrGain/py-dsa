
class Node:
    def __init__(self, data = None) -> None:
        self.data = data
        self.next = None

class singleList:
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
    
    def searchInList(self, key):
        index = 1
        current = self.head
        while current: 
            if current.data == key:
                return index
            index += 1
            current = current.next

        return -1

    def displayList(self):
        temp = self.head
        while temp:
            print(temp.data, end="-->")
            temp = temp.next
        print("None")
        return

if __name__ == "__main__":
    arr = [4, -3, 1, 0, 9, 11]
    llist = singleList()
    for i in arr:
        llist.Append(i)    
    llist.displayList() 
    result = llist.searchInList(key=4)  
    print("Element is found at index :",result)    
