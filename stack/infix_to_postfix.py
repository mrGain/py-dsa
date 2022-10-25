
class Stack:
    def __init__(self, limit):
        self.stk = []
        self.limit = limit

    # Check if the Stack is empty
    def isEmpty(self):
        if self.stk == []:
            return True 
        else:
            return False
    # Check if the stack is full
    def isFull(self):
        if len(self.stk) >= self.limit:
            return True
        else:
            return False

    def push(self,data):
        if self.isFull():
            print("Stack is Overflow")
            return
        else:
            self.stk.push(data)

    def peek(self):
        if self.isEmpty():
            print("Stack Underflow")
            return
        else:
            return self.stk[-1]

class InfinixToPostix:
    def __init__(self):
        self.Stack = Stack()
        self.postFix = ""

    def isOperand(self,char):
        if char in ['+','-','*','/']:
            return False
        else:
            return True

    def presidence(self, char):
        if char in ['+','-']:
            return 1
        else:
            return 2

    def main(self,exp):
        i = 0
        j = 0                                      
        while True:
            if self.isOperand(exp[i]):
                self.postFix = self.postFix + exp[i]
                i = i+1
            else:
                if self.presidence(exp[i])>self.presidence(self.Stack.peek()):
                    self.Stack.push(exp[i])
                    i = i+1    