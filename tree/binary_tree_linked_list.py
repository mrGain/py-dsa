class TreeNode:
    def __init__(self,data):
        self.leftChild = None 
        self.data = data 
        self.rightChild = None 

newBT = TreeNode('Dtinks')
leftChild = TreeNode('Hot')        
rightChild = TreeNode('Cold')
newBT.leftChild = leftChild
newBT.rightChild = rightChild

# Pre-order Traversal ( root-->left-->right )
def preOrderTraversal(rootNode):
    if not rootNode:
        return 
    print(rootNode.data)
    preOrderTraversal(rootNode.leftChild)    
    preOrderTraversal(rootNode.rightChild)

preOrderTraversal(newBT)        

