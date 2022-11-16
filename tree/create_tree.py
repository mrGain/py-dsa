class TreeNode:
    def __init__(self, data, children):
        self.data = data 
        self.children = children

    def __str__(self, level = 0):
        ret = " " * level + self.data + '\n'

        for child in self.children:
            ret += child.__str__(level + 1)
        return ret 

    def addChild(self, TreeNode):
        self.children.append(TreeNode)

tree = TreeNode('Drinks', [])
cold = TreeNode('cold', [])
hot = TreeNode('hot',[])
tree.addChild(cold)
tree.addChild(hot)
print(tree) 
tea = TreeNode('Tea',[])               
coffee = TreeNode('Coffee',[])
hot.addChild(tea)
hot.addChild(coffee)
print(tree) 

soft = TreeNode('soft',[])
soda = TreeNode('soda',[])
cold.addChild(soft)
cold.addChild(soda)
print(tree)
