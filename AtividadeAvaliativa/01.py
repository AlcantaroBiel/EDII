class Node:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None

def inorder(root_node, arr):
    current = root_node
    if current is None:
        return
    
    inorder(current.left, arr)
    arr.append(current)
    inorder(current.right, arr)


def preorder(root_node, arr):
    current = root_node
    if current is None:
        return

    arr.append(current)
    preorder(current.left, arr)
    preorder(current.right, arr)

def postorder(root_node, arr):
    current = root_node
    if current is None:
        return

    postorder(current.left, arr)
    postorder(current.right, arr)
    arr.append(current)
        
#Inserção dados
n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)
n5 = Node(5)
n6 = Node(6)
n7 = Node(7)
n8 = Node(8)

n1.left = n2
n1.right = n3
n2.left = n4
n3.left = n5
n3.right = n6
n5.left = n7
n5.right = n8

arrInOrder = []
arrPreOrder = []
arrPostOrder = []



print("\nExercício A:")
inorder(n1, arrInOrder)
print("Em-Ordem:", ' -> '.join(str(node.data) for node in arrInOrder))

print("\nExercício B:")
preorder(n1, arrPreOrder)
print("Pré-Ordem:", ' -> '.join(str(node.data) for node in arrPreOrder))

print("\nExercício C:")
postorder(n1, arrPostOrder)
print("Pós-Ordem:", ' -> '.join(str(node.data) for node in arrPostOrder))