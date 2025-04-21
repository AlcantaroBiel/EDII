class Node:
    def __init__(self,data):
        self.data = data
        self.right_child = None
        self.left_child = None

n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)
n5 = Node(5)
n6 = Node(6)
n7 = Node(7)
n8 = Node(8)

n1.left_child = n2
n1.right_child = n3
n3.right_child = n6
n3.left_child = n5
n2.left_child = n4
n5.left_child = n7
n5.right_child = n8

def inorder(root_node, arr):
    current = root_node
    if current is None:
        return
    
    inorder(current.left_child, arr)
    arr.append(current)
    inorder(current.right_child, arr)

arrInOrder = []

inorder(n1, arrInOrder)
print("Em ordem (esquerda, raiz, direita):", ' -> '.join(str(node.data) for node in arrInOrder))

def postorder(root_node, arr):
    current = root_node
    if current is None:
        return
 
    postorder(current.left_child, arr)
    postorder(current.right_child, arr)
    arr.append(current)

arrPostOrder = []

postorder(n1, arrPostOrder)
print("Pós ordem (esquerda, direita, raiz):", ' -> '.join(str(node.data) for node in arrPostOrder))