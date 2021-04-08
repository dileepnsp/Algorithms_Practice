class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

root=Node(10)

root.left=Node(34)
root.right=Node(89)

root.left.left=Node(20)
root.left.right=Node(45)

root.right.left=Node(56)
root.right.right=Node(54)


# Traversal:
#Inorder Traversal
#the left child is visited first, followed by the right child, then followed by the parent node
# For the tree,
#          10
#        /    \
#       34      89
#     /    \  /    \
#  20     45  56    54

# Inorder traversal: 20 34 45 10 56 89 54
def inorder(node):
    if node:
        inorder(node.left)
        print(node.data)
        inorder(node.right)
inorder(root)

