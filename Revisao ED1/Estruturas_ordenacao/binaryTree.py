class Node:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None

n1 = Node("Root node")
n2 = Node("Node Child Left")
n3 = Node("Node Child Right")
n4 = Node("Left Grandchild Node")

n1.left = n2
n1.right = n3
n2.left = n4

# current = n1
# while current:
#     print(current.data)
#     current = current.left

def inorder(root_node):
    current = root_node
    if current is None:
        return
    
    inorder(current.left)
    print(current.data)
    inorder(current.right)


def preorder(root_node):
    current = root_node
    if current is None:
        return

    print(current.data)
    preorder(current.left)
    preorder(current.right)

def postorder(root_node):
    current = root_node
    if current is None:
        return

    postorder(current.left)
    postorder(current.right)
    print(current.data)

inorder(n1)
print("\n")
preorder(n1)
print("\n")
postorder(n1)