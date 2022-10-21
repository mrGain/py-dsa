class Node:
    def __init__(self, data=None):
        self.data = data
        self.prev = None
        self.next = None

class DoublyList:
    def __init__(self):
        self.head = None
        self.tail = None

    def Insert(self,new_data,position=None):
        new_node = Node(new_data)
        if self.head == None and position == None:
            self.head = new_node
            self.tail = new_node
            return 

        if position == 1:
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node

        if position == None:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node  

        if position != None and position > 1:
            temp = self.head
            for i in range(1,position-1):
                temp = temp.next
            new_node.prev = temp
            new_node.next = temp.next
            temp.next = new_node    
        return

    def displayList(self):
        temp = self.head
        while temp:
            print(temp.data,end="-->")
            temp = temp.next
        return            

    # Delete form a doubly linked list
    def DeleteNode(self,position):
        if self.head == None:
            print("The linked list not exist")
            return
        if position == 1:
            if self.head == self.tail:
                self.head,self.tail = None,None
            else:
                self.head = self.head.next
            return

        temp = self.head
        for i in range(1,position-1):
            temp = temp.next

        if temp.next == self.tail:
            self.tail = self.tail.prev
            self.tail.next = None

        else:
            temp.next = temp.next.next
            temp.next.prev = temp                
        return


dll = DoublyList()
dll.Insert(10)
dll.Insert(30)
dll.Insert(20)
dll.Insert(13)
dll.Insert(8)
dll.displayList()
# dll.Insert(43,3)
# # dll.Insert(60,1)
# print()
# dll.displayList()
dll.DeleteNode(4)
print()
dll.displayList()


