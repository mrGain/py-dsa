
from queue import queue_linked_list as queue  # TO run relative import always do python3 -m tree.<name_of _file>
class TreeNode:
    def __init__(self,data) -> None:
        self.lchild = None
        self.data = data
        self.rchild = None

    def leftChild(self,data):
        lchild = TreeNode(data)
        self.lchild = lchild
    def rightChild(self,data):
        rchild = TreeNode(data)
        self.rchild = rchild

    def levelOrderTraversal(self):
        if self is None:
            print("No Node")
            return
        q = queue.Queue()
        q.enQueue(self)

        while q.isEmpty() != True:
            root = q.deQueue()
            print(root.data)
            if root.lchild is not None:
                q.enQueue(root.lchild)
            if root.rchild is not None:
                q.enQueue(root.rchild)

    def BTSearch(self,key):
        q = queue.Queue()
        q.enQueue(self)
        while q.isEmpty() != True:
            root = q.deQueue()
            if root.data == key:
                return True
            if root.lchild is not None:
                q.enQueue(root.lchild)
            if root.rchild is not None:
                q.enQueue(root.rchild)
                
        return False        


if __name__ == "__main__":
    newBT = TreeNode(10)
    # newBT.levelOrderTraversal()
    newBT.leftChild(20)
    newBT.rightChild(30)
    newBT.lchild.leftChild(40)
    newBT.lchild.rightChild(50)
    newBT.rchild.leftChild(60)
    newBT.rchild.rightChild(70)
    newBT.levelOrderTraversal()
    print(newBT.BTSearch(90))
