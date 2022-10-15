
class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class Linkedlist:
    def __init__(self):
        self.head = None

    def insert_at_begining(self, data):
        node = Node(data, self)
        self.head = node
    
    def print(self):
        if self.head is None:
            print("Linked list is empty...!")
            return 

        itr = self.head
        llstr = ''   
        while itr:
            llist = str(itr.data) + "-->"
            itr = itr.next

        print(llist)      


if __name__ == "__main__":
    llist = Linkedlist()

    llist.head = Node(10)
    second = Node(20)
    third = Node(30)

    llist.head.next = second
    second.next = third
