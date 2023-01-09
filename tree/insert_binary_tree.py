from queue import queue_linked_list as queue  # TO run relative import always do python3 -m tree.<name_of _file>

class TreeNode:
    def __init__(self,data) -> None:
        self.lchild = None
        self.data = data
        self.rchild = None

    def insertBT(self,newNode):
        q = queue.Queue()
        q.enQueue(self)
        while q.isEmpty() != True:
            root = q.deQueue()
            if root.lchild != None:
                q.enQueue(root.lchild)
            else:
                root.lchild = newNode
                return "Successfully inserted"
            if root.rchild != None:
                q.enQueue(root.rchild)
            else:
                root.rchild = newNode
                return "Successfully inserted"

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

if __name__ == "__main__":
    bt = TreeNode(10)
    bt.insertBT(TreeNode(20))
    bt.insertBT(TreeNode(30))
    bt.insertBT(TreeNode(40))
    bt.insertBT(TreeNode(50))
    bt.levelOrderTraversal()  

