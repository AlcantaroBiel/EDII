import queue

fila_fifo = queue.Queue()
fila_fifo.put('Primeiro da Fila')
fila_fifo.put('Segundo da Fila')
print(fila_fifo.qsize())
print(fila_fifo.get())
print(fila_fifo.get())
print(fila_fifo.qsize())

fila_lifo = queue.LifoQueue()
fila_lifo.put('Primeiro da Fila')
fila_lifo.put('Segundo da Fila')
fila_lifo.put('Terceiro da Fila')
print(fila_lifo.get())
print(fila_lifo.get())

fila_priority = queue.PriorityQueue()
fila_priority.put(2, 'Primeiro a Fila')
fila_priority.put(3, 'Segundo a Fila')
fila_priority.put(1, 'Terceiro a Fila')
print(fila_priority.get())
print(fila_priority.get())