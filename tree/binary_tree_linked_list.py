class TreeNode:
    def __init__(self,data):
        self.leftChild = None 
        self.data = data 
        self.rightChild = None 


# Pre-order Traversal ( root-->left-->right )
def preOrderTraversal(rootNode):
    if not rootNode:
        return 
    print(rootNode.data)
    preOrderTraversal(rootNode.leftChild)    
    preOrderTraversal(rootNode.rightChild)

 

# InOrder traversal ( left-->root-->right )
def inOrderTraversal(rootNode):
    if not rootNode:
        return
    inOrderTraversal(rootNode.leftChild)
    print(rootNode.data)
    inOrderTraversal(rootNode.rightChild)

    
newBT = TreeNode('Dtinks')
leftChild = TreeNode('Hot')        
rightChild = TreeNode('Cold')
newBT.leftChild = leftChild
newBT.rightChild = rightChild


preOrderTraversal(newBT)   

inOrderTraversal(newBT)