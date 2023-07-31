def selection_sort(lista):
    contador = 0
    for i in range(len(lista)-1):
        menor = i
        for j in range(i+1, len(lista)):
            if lista[j] < lista[menor]:
                menor = j
        contador += 2
        lista[i], lista[menor] = lista[menor], lista[i]
    return contador


lista = [2, 9, 3, 4, 1]
print(selection_sort(lista))
print(lista)
