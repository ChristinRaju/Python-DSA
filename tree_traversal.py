class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self, root):
        self.root = Node(root)

    def inorder(self, node):
        if node:
            self.inorder(node.left)
            print(node.value, end=" ")
            self.inorder(node.right)

    def preorder(self, node):
        if node:
            print(node.value, end=" ")
            self.preorder(node.left)
            self.preorder(node.right)

    def postorder(self, node):
        if node:
            self.postorder(node.left)
            self.postorder(node.right)
            print(node.value, end=" ")

tree = BinaryTree("1")
tree.root.left = Node("2")
tree.root.right = Node("3") 
tree.root.left.left = Node("4")
tree.root.left.right = Node("5")

print("Inorder traversal:")
tree.inorder(tree.root)
print("\nPreorder traversal:")
tree.preorder(tree.root)
print("\nPostorder traversal:")
tree.postorder(tree.root)



#The binary tree structure is as follows:
    #     1
    #    / \
    #   2   3
    #  / \
    # 4   5
