def busca_linear(L, x):
    achou = False
    i = 0
    while i < len(L) and  not achou:
        if(L[i] == x):
            achou == True
            pos = i
        else:
            i = i + 1

        if achou:
            return pos
        else:
            return achou
        
L = [12, 99, 37, 24, 2, 15]
result = busca_linear(L, 2)
print(result)