class MaxHeap:
    def __init__(self):
        self.heap = []  # A heap é representada por uma lista

    # Função para obter o índice do pai de um nó
    def _parent(self, index):
        return (index - 1) // 2

    # Função para obter o índice do filho à esquerda
    def _left(self, index):
        return 2 * index + 1

    # Função para obter o índice do filho à direita
    def _right(self, index):
        return 2 * index + 2

    # Troca dois elementos da heap
    def _swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    # Sobe o valor na heap para manter a propriedade de Max Heap
    def _heapify_up(self, index):
        while index > 0 and self.heap[index] > self.heap[self._parent(index)]:
            self._swap(index, self._parent(index))
            index = self._parent(index)

    # Desce o valor na heap para manter a propriedade de Max Heap
    def _heapify_down(self, index):
        largest = index
        left = self._left(index)
        right = self._right(index)

        if left < len(self.heap) and self.heap[left] > self.heap[largest]:
            largest = left

        if right < len(self.heap) and self.heap[right] > self.heap[largest]:
            largest = right

        if largest != index:
            self._swap(index, largest)
            self._heapify_down(largest)

    # Inserção de um novo valor
    def insert(self, value):
        self.heap.append(value)
        self._heapify_up(len(self.heap) - 1)

    # Remove e retorna o maior valor (a raiz da heap)
    def extract_max(self):
        if not self.heap:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()

        max_value = self.heap[0]
        # Coloca o último valor na raiz e faz o heapify
        self.heap[0] = self.heap.pop()
        self._heapify_down(0)
        return max_value

    # Remove um valor específico da heap
    def remove(self, value):
        try:
            index = self.heap.index(value)
        except ValueError:
            return False  # Valor não está na heap

        # Substitui pelo último elemento
        self.heap[index] = self.heap[-1]
        self.heap.pop()

        # Corrige a heap (pra cima ou pra baixo)
        if index < len(self.heap):
            self._heapify_up(index)
            self._heapify_down(index)
        return True

    # Exibe o conteúdo da heap
    def show(self):
        print("Heap:", self.heap)

heap = MaxHeap()

# Inserção
heap.insert(20)
heap.insert(15)
heap.insert(30)
heap.insert(40)
heap.insert(10)
heap.show()  # Deve estar organizada com o maior valor no topo

# Remoção da raiz (maior valor)
print("Removido (raiz):", heap.extract_max())
heap.show()

# Remoção de um valor específico
print("Removido: 15")
heap.remove(15)
heap.show()
