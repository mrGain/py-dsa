class Stack:
    def __init__(self,limit):
        self.stk = []
        self.limit = limit

    def __str__(self):
        values = self.stk.reverse()
        values = [str(x) for x in self.stk]
        return '\n'.join(values)

    # Check if the Stack is empty or not 
    def isEmpty(self):
        if self.stk == []:
            return True
        else:
            return False 


    def push(self, value):
        self.stk.append(value)
        return "The element has been successfully inserted"

    def pop(self):
        if self.isEmpty():
            return "There is not any element in the Stack"
        else:
            return self.stk.pop()        

our_stack = Stack(10)
# print(our_stack.isEmpty())
our_stack.push(10)
our_stack.push(20)
our_stack.push(30)
print(our_stack)