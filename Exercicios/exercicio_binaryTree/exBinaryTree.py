class Node:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None

n1 = Node("A")
n2 = Node("B")
n3 = Node("C")
n4 = Node("D")
n5 = Node("E")
n6 = Node("F")
n7 = Node("G")
n8 = Node("H")

n1.left = n2
n1.right = n3
n2.left = n4
n2.right = n5
n3.right = n6
n4.left = n7
n4.right = n8


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