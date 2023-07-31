def busca_binaria(lista, elemento):
    inicio = 0
    contador = 0
    fim = len(lista) - 1
    while inicio <= fim:
        meio = (inicio + fim) // 2
        contador += 1
        if elemento == lista[meio]:
            return meio, contador
        elif elemento > lista[meio]:
            inicio = meio + 1
        else:
            fim = meio - 1
    return -1, contador

lista = [11, 22, 33, 44, 55, 66, 77, 88, 99]
print(busca_binaria(lista, 0))
print(busca_binaria(lista, 11))
print(busca_binaria(lista, 55))
print(busca_binaria(lista, 77))
print(busca_binaria(lista, 44))
print(busca_binaria(lista, 67))