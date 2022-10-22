
class Node:
    def __init__(self, data = None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

class Stack:
    def __init__(self):
        self.LinkedList = LinkedList()

    # Check wether the List is Empty
    def isEmpty(self):
        if self.LinkedList.head == None:
            return True
        else:
            return False 

    # Pushing the data to the stack
    def push(self,data):
        node = Node(data)
        node.next = self.LinkedList.head
        self.LinkedList.head = node 

        return
    
    # Pooping the data from the stack
    def pop(self):
        ''' This will remove and return the last inserted element form the Stack '''
        if self.isEmpty():
            return "There is not any element in the Stack"
            
        else:
            nodeValue = self.LinkedList.head.data
            self.LinkedList.head = self.LinkedList.head.next
            return nodeValue
        

    # Peeking the Top most element form the Stack
    def peek(self):
        if self.isEmpty():
            return "there si not any element in the stack"
        else:
            return self.LinkedList.head.data

    # Printign the Stack
    def printStack(self):
        if self.isEmpty():
            print("Stack is empty")
            return
        else:    
            temp = self.LinkedList.head
            while temp:
                print(temp.data)
                temp = temp.next 

        return    

    # Deleting the Stack
    def delete(self):
        self.LinkedList.head = None 
        return 'Stack deleted successfully'    

stk = Stack()
# print(stk.isEmpty())
stk.push(1)
stk.push(4)
stk.push(2)
stk.push(3)

stk.printStack()

# stk.pop()
print("---------")
# stk.printStack()

print(stk.peek())
stk.delete()
print(stk.isEmpty())