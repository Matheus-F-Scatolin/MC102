def insertion_sort(lista):
    contador = 0
    for i in range(1, len(lista)):
        posicao_atual = i
        aux = lista[i]
        while aux < lista[posicao_atual-1] and posicao_atual > 0:
            contador += 1
            lista[posicao_atual] = lista[posicao_atual-1]
            posicao_atual -= 1
        contador += 1
        lista[posicao_atual] = aux
    return contador



lista = [2, 9, 3, 4, 1]
print(insertion_sort(lista))
print(lista)


    