class Node:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None

class Tree:
    def __init__(self):
        self.root_node = None
    
    def insert(self, data):
        node = Node(data)

        if self.root_node is None:
            self.root_node = node
            return self.root_node
        else:
            current = self.root_node
            parent = None
            while True:
                parent = current
                if node.data < parent.data:
                    current = current.left
                    if current is None:
                        parent.left = node
                        return self.root_node
                else:
                    current = current.right
                    if current is None:
                        parent.right = node
                        return self.root_node


    def inorder(self, root_node):
        current = root_node
        if current is None:
            return
        
        self.inorder(current.left)
        print(current.data)
        self.inorder(current.right)

    def search(self, data):
        current = self.root_node
        if current is None:
            print("Item not found")
            return None
        elif current.data is data:
            print()

    def get_node(self, data):
        parent = None
        current = self.root_node
        if current is None:
            return (parent, None)

        while True:
            if current.data = data

tree = Tree()

n = tree.insert(5)
n = tree.insert(7)
n = tree.insert(3)
n = tree.insert(1)

inorder(tree.root_node)            