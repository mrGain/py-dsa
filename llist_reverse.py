

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class sLinkedList:
    def __init__(self):
        self.head = None

    # Function to insert/ append element in linked list
    def append(self, new_data):
        # Check if the head is None
        new_node = Node(new_data)
        if self.head is None:
            self.head = new_node
            return

        last = self.head
        while last.next:
            last = last.next
        
        last.next = new_node
        return

    def printList(self):
        temp = self.head
        while temp:
            print(temp.data, end="-->")
            temp = temp.next    
        return

    def reverseList(self):
        prev = None
        current = self.head
        while current is not None:
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev
        return    

if __name__ == "__main__":
    llist = sLinkedList()
    arr = [int(x) for x in input().split()]
    for i in arr:
        llist.append(i)        
    llist.printList()
    llist.reverseList()
    print()
    llist.printList()

#function Template for python3

"""
# Node Class

class node:
    def __init__(self, val):
        self.data = val
        self.next = None



class Solution:
    #Function to reverse a linked list.
    def reverseList(self, head):
        prev = None
        current = head
        while current is not None:
            next = current.next
            current.next = prev
            prev = current
            current = next
        head = prev
        return head



#{ 
 # Driver Code Starts
# Node Class    
class Node:
    def __init__(self, val):
        self.data = val
        self.next = None

# Linked List Class
class Linked_List:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert(self, val):
        if self.head is None:
            self.head = Node(val)
            self.tail = self.head
        else:
            self.tail.next = Node(val)
            self.tail = self.tail.next

def printList(head):
    tmp = head
    while tmp:
        print(tmp.data, end=' ')
        tmp=tmp.next
    print()

if __name__=='__main__':
    for i in range(int(input())):
        n = int(input())
        arr = [int(x) for x in input().split()]
        
        lis = Linked_List()
        for i in arr:
            lis.insert(i)
        
        newHead = Solution().reverseList(lis.head)
        printList(newHead)

# } Driver Code Ends

"""