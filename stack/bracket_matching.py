
class Stack:
    def __init__(self):
        self.stk = []
    
    def isEmpty(self):
        if self.stk == []:
            return True
        else:
            return False

    def push(self,char):
        self.stk.append(char)

    def pop(self):
        self.stk.pop() 

class Solution:
    def __init__(self):
        self.Stack = Stack()

    def isBalanced(self,expression):
        if expression == "":
            print("No expression given")
            return None

        for char in expression:
            if char in ["(","{","["]:
                self.Stack.push(char)
            elif char in [")","}","]"]:
                if self.Stack.isEmpty():
                    return False
                self.Stack.pop()

        return True if self.Stack.isEmpty() else False           


sol = Solution()
expr = ""
if sol.isBalanced(expr):
    print("Is Balanced")
else:
    print("Not Balanced")    