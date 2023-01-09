from queue import queue_linked_list as queue 

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

# post order traversal ( left --> right --> root )
def postOrderTraversal(rootNode):
    if not rootNode:
        return
    postOrderTraversal(rootNode.leftChild)
    postOrderTraversal(rootNode.rightChild)
    print(rootNode.data) 

def levelOrderTraversal(rootNode):
    if not rootNode:
        return
    else:
        customeQueue = queue.Queue()
        customeQueue.enQueue(rootNode)
        while not (customeQueue.isEmpty()):
            root = customeQueue.deQueue()
            print(root.data)
            if (root.leftChild is not None):
                customeQueue.enQueue(root.leftChild)
            if (root.rightChild is not None):
                customeQueue.enQueue(root.rightChild)    

if __name__ == "__main__":
    newBT = TreeNode('Dtinks')
    leftChild = TreeNode('Hot')        
    rightChild = TreeNode('Cold')
    tea = TreeNode('tea')
    coffee = TreeNode('coffee')
    leftChild.leftChild = tea
    leftChild.rightChild = coffee
    newBT.leftChild = leftChild
    newBT.rightChild = rightChild


    #preOrderTraversal(newBT)   

    #inOrderTraversal(newBT)

    #postOrderTraversal(newBT)
    levelOrderTraversal(newBT)