#implementation of BST
class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value
def insert(root, node):
    if root is None:
        root = node
    else:
        if node.value < root.value:
            if root.right is None:
                root.right = node
            else:
                insert(root.right, node)
        else:
            if root.left is None:
                root.left = node
            else:
                insert(root.left, node)
def inorder(root):
    if root:
        inorder(root.left)
        print(root.value)
        inorder(root.right)

r = Node(5)
insert(r, Node(10))
insert(r, Node(15))
insert(r, Node(3))
inorder(r)
