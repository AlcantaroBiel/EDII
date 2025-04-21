# Classe que representa um nó da árvore binária
class Node:
    def __init__(self, value):
        self.value = value      # Valor armazenado no nó
        self.left = None        # Referência para o filho à esquerda
        self.right = None       # Referência para o filho à direita

# Classe que representa a árvore binária
class BinaryTree:
    def __init__(self):
        self.root = None        # Inicialmente, a árvore está vazia

    # Insere um valor na árvore, se ele ainda não existir
    def insert(self, value):
        if self.exists(value):
            return False        # Não insere valores duplicados
        if self.root is None:
            self.root = Node(value)  # Se a árvore estiver vazia, cria a raiz
        else:
            self._insert(self.root, value)  # Insere recursivamente
        return True

    # Função auxiliar recursiva para inserir um valor
    def _insert(self, current, value):
        if value < current.value:
            if current.left is None:
                current.left = Node(value)  # Insere à esquerda
            else:
                self._insert(current.left, value)  # Continua procurando
        else:
            if current.right is None:
                current.right = Node(value)  # Insere à direita
            else:
                self._insert(current.right, value)

    # Verifica se um valor existe na árvore
    def exists(self, value):
        return self._exists(self.root, value)

    # Função auxiliar recursiva para verificar existência
    def _exists(self, current, value):
        if current is None:
            return False
        if current.value == value:
            return True
        elif value < current.value:
            return self._exists(current.left, value)
        else:
            return self._exists(current.right, value)

    # Remove um valor da árvore, se ele existir
    def remove(self, value):
        if not self.exists(value):
            return False  # Não faz nada se o valor não estiver na árvore
        self.root = self._remove(self.root, value)
        return True

    # Função auxiliar recursiva para remoção
    def _remove(self, current, value):
        if current is None:
            return None

        if value < current.value:
            current.left = self._remove(current.left, value)
        elif value > current.value:
            current.right = self._remove(current.right, value)
        else:
            # Caso com um filho ou nenhum
            if current.left is None:
                return current.right
            elif current.right is None:
                return current.left

            # Caso com dois filhos: substitui pelo menor da subárvore direita
            min_larger_node = self._get_min(current.right)
            current.value = min_larger_node.value
            current.right = self._remove(current.right, min_larger_node.value)

        return current

    # Retorna o menor nó a partir de um nó dado (usado na remoção)
    def _get_min(self, node):
        while node.left is not None:
            node = node.left
        return node

    # Percurso in-order: esquerda, raiz, direita
    def inOrder(self):
        results = []
        def _inOrder(node):
            if node is None:
                return
            _inOrder(node.left)
            results.append(str(node.value))
            _inOrder(node.right)  

        _inOrder(self.root)
        print(" ".join(results))

    # Percurso pre-order: raiz, esquerda, direita
    def preOrder(self):
        results = []
        def _preOrder(node):
            if node is None:
                return
            results.append(str(node.value))
            _preOrder(node.left)
            _preOrder(node.right)

        _preOrder(self.root)
        print(" ".join(results))

    # Percurso post-order: esquerda, direita, raiz
    def postOrder(self):
        results = []
        def _postOrder(node):
            if node is None:
                return
            _postOrder(node.left)
            _postOrder(node.right)
            results.append(str(node.value))

        _postOrder(self.root)
        print(" ".join(results))

#Exercício 1
#Criação árvore 1
tree1 = BinaryTree()
tree1.insert(8)
tree1.insert(2)
tree1.insert(9)
tree1.insert(1)
tree1.insert(6)
tree1.insert(10)
tree1.insert(5)

print("Exercício 1: Verifica o nó raíz por último")
tree1.postOrder()

#Exercício 2
#Criação árvore 
tree2 = BinaryTree()
tree2.insert(7)
tree2.insert(5)
tree2.insert(8)
tree2.insert(1)
tree2.insert(6)
tree2.insert(9)

print("\nExercício 2: \nEm-Ordem:")
tree2.inOrder()
print("Pré-Ordem:")
tree2.preOrder()
print("Pós-Ordem:")
tree2.postOrder()