def merge(arr, l, m, r):
    n1 = m - l + 1  # Tamanho do subarray esquerdo
    n2 = r - m  # Tamanho do subarray direito

    # Criação das sublistas
    L = [0] * (n1)
    R = [0] * (n2)

    # Copiar os dados para as sublistas L[] e R[]
    for i in range(n1):
        L[i] = arr[l + i]

    for j in range(n2):
        R[j] = arr[m + 1 + j]

    i, j, k = 0, 0, l  # Índices para as sublistas L, R e a lista principal

    # Mesclar as duas sublistas de volta em arr[]
    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1

    # Copiar os elementos restantes de L[], se houver
    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1

    # Copiar os elementos restantes de R[], se houver
    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1

def merge_sort(arr, l, r):
    if l < r:
        m = (l + r) // 2  # Encontrar o ponto médio
        merge_sort(arr, l, m)  # Ordenar a primeira metade
        merge_sort(arr, m + 1, r)  # Ordenar a segunda metade
        merge(arr, l, m, r)  # Mesclar as duas metades

# Testando o código
arr = [12, 11, 13, 5, 6, 7]
n = len(arr)

print("Matriz fornecida: ")
for i in range(n):
    print("%d" % arr[i], end=' ')

merge_sort(arr, 0, n - 1)

print('\n\nMatriz ordenada: ')
for i in range(n):
    print("%d" % arr[i], end=' ')
