from collections import deque

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

def lever_order_traversal(root_node):
    list_of_nodes = []
    traversal_queue = deque([root_node])
    while len(traversal_queue) > 0:
        node = traversal_queue.popleft()
        list_of_nodes.append(node.data)
        if node.left:
            traversal_queue.append(node.left)
            if node.right:
                traversal_queue.append(node.right)
    return list_of_nodes

print(lever_order_traversal(n1))