class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class sLinkedList:
    def __init__(self):
        self.head = None

    # function to insert new node at the begining
    def push(self, new_data):
        new_node = Node(new_data)
        # Make newxt of new node as head
        new_node.next = self.head
        self.head = new_node

    # Function to insert the node at any position 
    def insertAt(self,position,new_data):
        new_node = Node(new_data)

        if position<1 :
            print("\n Invalid position, try something else")

        elif position == 1:
            new_node.next = self.head
            self.head = new_data

        else:
            temp = self.head
            for i in range(1, position-1):
                if temp != None:
                    temp = temp.next
            if temp != None:        
                new_node.next = temp.next
                temp.next = new_node


    def append(self, new_data):
        # Create new node   
        # put in the data
        # set next as none
        new_node = Node(new_data)
        # If the Linked list is empty make the newnode as head
        if self.head is None:
            self.head = new_node
            return

        # Else traverse till the last node 
        last = self.head   
        while (last.next):
            last = last.next
        # Change the next of last node
        last.next = new_node
    


    def printList(self):
        temp = self.head
        while temp:
            print(temp.data,end="-->")
            temp = temp.next   
   

if __name__ == "__main__":
    llist = sLinkedList()
    llist.append(10)
    llist.append(20)
    llist.append(30)
    llist.push(55)

    llist.insertAt(3,60)

    print("Created Linked list is:")
    llist.printList()            