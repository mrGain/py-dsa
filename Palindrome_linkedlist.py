
'''
class Solution:
    def findMid(self, head):
        length = 0
        mid = 0

        temp = head
        while temp:
            temp = temp.next
            length += 1
        if length % 2 == 0:
            mid = length // 2
            print("if")
        else:
            mid = length // 2

        temp = head    
        for i in range(0,mid):
            temp = temp.next
        return temp.data      

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class sLinkedlist:
    def __init__(self):
        self.head = None
    # insert element in linked list
    def append(self, new_data):
        new_node = Node(new_data)
        if self.head is None:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node  

    def printList(self):
        temp = self.head
        while temp:
            print(temp.data, end=" ")
            temp = temp.next
        return     
                      

if __name__ == "__main__":
    llist = sLinkedlist()
    arr = [int(x) for x in input().split()]
    for elem in arr:
        llist.append(elem)

    llist.printList() 
    ob = Solution()
    print(ob.findMid(llist.head))   

'''

#User function Template for python3 praxctice geeks for geeks
'''
	Your task is to check if given linkedlist
	is a pallindrome or not.
	
	Function Arguments: head (reference to head of the linked list)
	Return Type: boolean , no need to print just return True or False.

	{
		# Node Class
		class Node:
		    def __init__(self, data):   # data -> value stored in node
		        self.data = data
		        self.next = None
	}

	Contributed By: Nagendra Jha
'''
#Function to check whether the list is palindrome.
class Solution:
    def isPalindrome(self, head):
        count = 0
        arr = []
        while head:
            count += 1
            arr += [head.data]
            head = head.next

        if arr == arr[::-1] :
            return True
        return False        

#{ 
 # Driver Code Starts
#Initial Template for Python 3
#Contributed by : Nagendra Jha

import atexit
import io
import sys

class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None

# Linked List Class
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    # creates a new node with given value and appends it at the end of the linked list
    def append(self, new_value):
        new_node = Node(new_value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return
        self.tail.next = new_node
        self.tail = new_node 

if __name__ == '__main__':
    t=int(input())
    for cases in range(t):
        n = int(input())
        a = LinkedList() # create a new linked list 'a'.
        nodes_a = list(map(int, input().strip().split()))
        for x in nodes_a:
            a.append(x)  # add to the end of the list

        if Solution().isPalindrome(a.head):
            print(1)
        else:
            print(0)
# } Driver Code Ends