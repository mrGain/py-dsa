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
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = self.tail.next
        return  

    # Reverse the List using Recursion
    def reverseList(self,q,p):
        if p != None:
            self.reverseList(p,p.next)
            p.next = q
        else:
            self.head = q    

        
        return


    def diplayList(self):
        temp = self.head
        while temp:
            print(temp.data, end= "-->")
            temp = temp.next
        print("None")

        return   

if __name__ == "__main__":
    llist = SingleList()
    arr = [10,23,4,6,89]
    for i in arr:
        llist.Append(i)
    llist.diplayList()
    llist.reverseList(None,llist.head) 
    llist.diplayList()       