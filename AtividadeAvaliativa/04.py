class Node:
    def __init__(self,data):
        self.data = data
        self.right_child = None
        self.left_child = None

n1 = Node("1")
n2 = Node("2")
n3 = Node("3")
n4 = Node("4")
n5 = Node("5")
n6 = Node("6")
n7 = Node("7")
n8 = Node("8")
n9 = Node("9")

n1.left_child = n2
n1.right_child = n3
n3.right_child = n7
n3.left_child = n6
n2.left_child = n4
n2.right_child = n5
n6.left_child = n8
n6.right_child = n9

def imprimir_caminho_folha_raiz(root_node):
    if not root_node:
        return
    
    pilha = [(root_node,[])]

    while pilha:
        node, caminho = pilha.pop()
        novo_caminho = caminho + [node.data]

        if node.left_child is None and node.right_child is None:
            print(" -> ".join(map(str, reversed(novo_caminho))))
        else:
            if node.left_child:
                pilha.append((node.left_child, novo_caminho))
            if node.right_child:
                pilha.append((node.right_child, novo_caminho))

imprimir_caminho_folha_raiz(n1)