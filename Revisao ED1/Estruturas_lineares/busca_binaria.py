def busca_binaria(L, X):
    if len(L) == 0:
        return
    else:
        meio_list = len(L) // 2

        if L[meio_list] == X:
            return True
        elif X > L[meio_list]:
            return busca_binaria(L[meio_list +1:], X)
        elif X < L[meio_list]:
            return busca_binaria(L[:meio_list], X)
        
L = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(busca_binaria(L, 7))

        
