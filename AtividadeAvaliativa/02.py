class Node:
    def __init__(self, data):
        self.data = data
        self.left_child = None
        self.right_child = None

def verifica_iden(a, b):
    if a is None and b is None:
        return True, "Ambas as árvores têm a mesma estrutura e o mesmo conteúdo."
    
    if a is None or b is None:
        return False, "As árvores tem estruturas diferentes."
    
    if a.data != b.data:
        return False, f"As árvores tem a mesma estrutura, porém com valores de nós diferentes."
    
    esquerda_igual, motivo_esq = verifica_iden(a.left_child, b.left_child)
    if not esquerda_igual:
        return False, motivo_esq

    direita_igual, motivo_dir = verifica_iden(a.right_child, b.right_child)
    if not direita_igual:
        return False, motivo_dir

    return True, "Ambas as árvores têm a mesma estrutura e o mesmo conteúdo"


#Exemplo A - Árvores iguais
node1 = Node(1)
node1.left_child = Node(2)
node1.right_child = Node(3)
node1.left_child.left_child = Node(4)
node1.left_child.right_child = Node(5)
node1.right_child.left_child = Node(6)
node1.right_child.right_child = Node(7)

node2 = Node(1)
node2.left_child = Node(2)
node2.right_child = Node(3)
node2.left_child.left_child = Node(4)
node2.left_child.right_child = Node(5)
node2.right_child.left_child = Node(6)
node2.right_child.right_child = Node(7)

print("Exemplo A - Árvores iguais")
resultado, mensagem = verifica_iden(node1, node2)
print(resultado, "-", mensagem)

"Exemplo B - Estruturas Diferentes"
node1 = Node(1)
node1.left_child = Node(2)
node1.right_child = Node(3)
node1.left_child.left_child = Node(4)
node1.left_child.right_child = Node(5)
node1.right_child.left_child = Node(6)
node1.right_child.right_child = Node(7)

node2 = Node(1)
node2.left_child = Node(2)
node2.right_child = Node(3)
node2.left_child.left_child = Node(4)
node2.left_child.right_child = Node(5)
node2.right_child.left_child = Node(6)

print("Exemplo B - Estruturas Diferentes")
resultado, mensagem = verifica_iden(node1, node2)
print(resultado, "-", mensagem)

"Exemplo C - Conteúdos Diferentes"
node1 = Node(1)
node1.left_child = Node(2)
node1.right_child = Node(3)
node1.left_child.left_child = Node(4)
node1.left_child.right_child = Node(5)
node1.right_child.left_child = Node(6)
node1.right_child.right_child = Node(7)

node2 = Node(1)
node2.left_child = Node(2)
node2.right_child = Node(3)
node2.left_child.left_child = Node(4)
node2.left_child.right_child = Node(5)
node2.right_child.left_child = Node(6)
node2.right_child.right_child = Node(8)

print("Exemplo C - Conteúdos Diferentes")
resultado, mensagem = verifica_iden(node1, node2)
print(resultado, "-", mensagem)