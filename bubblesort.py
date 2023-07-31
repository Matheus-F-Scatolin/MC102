def bubble_sort(lista):
    contador = 0
    for i in range(len(lista)-1):
        ocorreu_troca = False
        for j in range(len(lista)-1, i, -1):
            if lista[j] < lista[j-1]:
                contador += 2
                lista[j], lista[j-1] = lista[j-1], lista[j]
                ocorreu_troca = True
        if not ocorreu_troca:
            break
    return contador


lista = [2, 9, 3, 4, 1]
print(bubble_sort(lista))
print(lista)
