# class Stack:
#     def __init__(self,limit):
#         self.stk = []
#         self.limit = limit

#     def __str__(self):
#         values = self.stk.reverse()
#         values = [str(x) for x in self.stk]
#         return '\n'.join(values)

#     # Check if the Stack is empty or not 
#     def isEmpty(self):
#         if self.stk == []:
#             return True
#         else:
#             return False 


#     def push(self, value):
#         self.stk.append(value)
#         return "The element has been successfully inserted"

#     def pop(self):
#         if self.isEmpty():
#             return "There is not any element in the Stack"
#         else:
#             return self.stk.pop()        

# our_stack = Stack(10)
# # print(our_stack.isEmpty())
# our_stack.push(10)
# our_stack.push(20)
# our_stack.push(30)
# print(our_stack)


class Stack:
    def __init__(self,limit):
        self.stk = []
        self.limit = limit
    
    # For printing the sack element
    def __str__(self):
        return ' '.join([str(i) for i in self.stk])

    # Check if the stack is Empty
    def isEmpty(self):
        if self.stk == []:
            return True
        else:
            return False
    # Check if the Stack is full
    def isFull(self):
        if len(self.stk) >= self.limit:
            return True
        else:
            return False 

    # For pushing an element on to the stack
    def push(self,data):
        if self.isFull():
            print("Stack Overflow")
        else:
            self.stk.append(data)

    # For pooping the uppermost element
    def pop(self):
        if self.isEmpty():
            print("Stack Underflow")
        else:
            return self.stk.pop()    
    # For peeking the top most element form the stack
    def peek(self):
        if self.isEmpty():
            return "There is not any elemnt in the stack"
        else:
            return self.stk[-1]

    # Deleting the entire Stack
    def delete(self):
        self.stk = None

        
mystack = Stack(limit=10)
mystack.push(20)                    
mystack.push(9)                    
mystack.push(7)  
print(mystack)  
mystack.pop()
print()
print(mystack.peek()) 
# print(mystack) 
                