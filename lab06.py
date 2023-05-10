def ad_elementos_neutros(vetor_1: list[int], vetor_2: list[int],
                         elem_neutro: int, div_inteira:
                         bool = False) -> list[list[int]]:
    """
    Ajusta o comprimento dos vetores para que sejam iguais.

    Caso o comprimento de vetor_1 seja maior que o de vetor_2, insere
    elementos neutros no vetor_2 até que ambos os vetores tenham o
    mesmo comprimento, e vice-versa. O valor do elemento neutro é
    determinado pela variável elem_neutro e pela variável div_inteira,
    que, quando tem valor "True", faz com que sejam adicionados uns no
    segundo vetor, ou zeros no primeiro.

    Parametros:
        vetor_1 (list): O primeiro vetor.
        vetor_2 (list): O segundo vetor.
        div_inteira (bool, optional): Variável para indicar a divisão
        inteira entre os vetores
        elem_neutro (int): Valor do elemento neutro a ser inserido nos
        vetores, caso div_inteira seja False.

    Retorna:
        dois novos vetores com dimensões corrigidas
    """
    if len(vetor_1) > len(vetor_2):
        for c in range(len(vetor_1) - len(vetor_2)):
            if div_inteira:
                elem_neutro = 1
            vetor_2.append(elem_neutro)
    if len(vetor_1) < len(vetor_2):
        for c in range(len(vetor_2) - len(vetor_1)):
            if div_inteira:
                elem_neutro = 0
            vetor_1.append(elem_neutro)
    return [vetor_1, vetor_2]


def soma_vetores(vetor_1: list[int], vetor_2: list[int]) -> list[int]:
    '''
    Retorna a soma de dois vetores.

    Os vetores devem ter o mesmo comprimento. Caso contrário, são adicionados
    elementos neutros (0) no menor vetor.

    Parametros:
        vetor_1 (list): O primeiro vetor.
        vetor_2 (list): O segundo vetor.

    Retorna:
        list: O vetor resultante da soma.
    '''
    vetor_1, vetor_2 = ad_elementos_neutros(vetor_1, vetor_2, 0)
    vetor_resultante = []
    for c in range(len(vetor_1)):
        vetor_resultante.append(vetor_1[c] + vetor_2[c])
    print(vetor_resultante)
    return vetor_resultante


def subtrai_vetores(vetor_1: list[int], vetor_2: list[int]) -> list[int]:
    '''
    Retorna a subtração de dois vetores.

    Os vetores devem ter o mesmo comprimento. Caso contrário, são adicionados
    elementos neutros (0) em ambos os vetores até que tenham o mesmo
    comprimento.

    Parametros:
        vetor_1 (list): O primeiro vetor.
        vetor_2 (list): O segundo vetor.

    Retorna:
        list: O vetor resultante da subtração.
    '''
    vetor_1, vetor_2 = ad_elementos_neutros(vetor_1, vetor_2, 0)
    vetor_resultante = []
    for c in range(len(vetor_1)):
        vetor_resultante.append(vetor_1[c] - vetor_2[c])
    print(vetor_resultante)
    return vetor_resultante


def multiplica_vetores(vetor_1: list[int], vetor_2: list[int]) -> list[int]:
    '''
    Retorna o produto elemento a elemento de dois vetores.

    Os vetores devem ter o mesmo comprimento. Caso contrário, são adicionados
    elementos neutros (1) em ambos os vetores até que tenham o mesmo
    comprimento.

    Parametros:
        vetor_1 (list): O primeiro vetor.
        vetor_2 (list): O segundo vetor.

    Retorna:
        list: O vetor resultante da multiplicação elemento a elemento.
'''
    vetor_1, vetor_2 = ad_elementos_neutros(vetor_1, vetor_2, 1)
    vetor_resultante = []
    for c in range(len(vetor_1)):
        vetor_resultante.append(vetor_1[c] * vetor_2[c])
    print(vetor_resultante)
    return vetor_resultante


def divide_vetores(vetor_1: list[int], vetor_2: list[int]) -> list[int]:
    '''
    Retorna o resultado da divisão inteira de dois vetores.

    Os vetores devem ter o mesmo comprimento. Caso contrário,
    são adicionados elementos neutros (0 ou 1) até que os vetores
    tenham o mesmo comprimento.

    Parametros:
        vetor_1 (list): O primeiro vetor.
        vetor_2 (list): O segundo vetor.

    Retorna:
        list: O vetor resultante da divisão.
    '''
    vetor_1, vetor_2 = ad_elementos_neutros(vetor_1, vetor_2, 0, True)
    vetor_resultante = []
    for c in range(len(vetor_1)):
        vetor_resultante.append(vetor_1[c] // vetor_2[c])
    print(vetor_resultante)
    return vetor_resultante


def multiplicacao_escalar(vetor: list[int], escalar: int) -> list[int]:
    '''
    Multiplica um vetor por um escalar.

    Parametros:
        vetor (list): O vetor que será multiplicado.
        escalar (int): O valor do escalar a ser multiplicado.

    Retorna:
        list: O vetor resultante da multiplicação.
    '''
    for c in range(len(vetor)):
        vetor[c] *= escalar
    print(vetor)
    return vetor


def n_duplicacao(vetor: list[int], n: int) -> list[int]:
    '''
    Retorna uma lista com todos os elementos do vetor repetidos n vezes.

    Parametros:
        vetor (list): O vetor que será duplicado.
        n (int): O número de vezes que cada elemento deve ser repetido.

    Retorna:
        list: A lista resultante com todos os elementos do vetor duplicados
        n vezes.
    '''
    if n == 0:
        print([])
        return []
    else:
        vetor_resultante = []
        for c in range(n):
            for elemento in vetor:
                vetor_resultante.append(elemento)
        print(vetor_resultante)
        return vetor_resultante


def soma_elementos(vetor: list[int]) -> int:
    '''
    Soma todos os elementos de um vetor.

    Parametros:
        vetor (list): O vetor a ser somado.

    Retorna:
        int: A soma dos elementos do vetor.
    '''
    soma = 0
    for elemento in vetor:
        soma += elemento
    print([soma])
    return soma


def produto_interno(vetor_1: list[int], vetor_2: list[int],
                    cor_cruzada: bool = False) -> int:
    '''
    Calcula o produto interno entre dois vetores.

    Parametros:
        vetor_1 (list): O primeiro vetor.
        vetor_2 (list): O segundo vetor.
        cor_cruzada (bool, optional): Indica que a função foi chamada pela
        função de correlação cruzada (nesse caso, ela não imprime nada)

    Retorna:
        int: O produto interno entre os dois vetores.
    '''
    ad_elementos_neutros(vetor_1, vetor_2, 1)
    soma = 0
    for c in range(len(vetor_2)):
        soma += vetor_1[c] * vetor_2[c]
    if not cor_cruzada:
        print([soma])
    return soma


def multiplica_todos(vetor_1: list[int], vetor_2: list[int]) -> list[int]:
    '''
    Multiplica todos os elementos de um vetor por um determinado
    elemento em outro vetor e soma os resultados.

    Parametros:
        vetor_1 (list): O primeiro vetor.
        vetor_2 (list): O segundo vetor.

    Retorna:
        list: Uma lista contendo os resultados da multiplicação e soma
        dos elementos correspondentes.
    '''
    vetor_resultante = []
    for elemento in vetor_1:
        soma = 0
        for elemento2 in vetor_2:
            soma += elemento*elemento2
        vetor_resultante.append(soma)
    print(vetor_resultante)
    return vetor_resultante


def correlacao_cruzada(vetor: list[int], mascara: list[int]) -> list[int]:
    '''
    Calcula a correlação cruzada entre um vetor e uma máscara.

    Parametros:
        vetor (list): lista contendo o vetor a ser correlacionado.
        mascara (list): lista contendo a máscara a ser utilizada na correlação.

    Retorna:
        list: lista contendo os valores da correlação cruzada
        para cada posição possível do vetor.
    '''
    vetor_resultante = []
    for c in range(len(vetor) - len(mascara) + 1):
        prod_interno = produto_interno(vetor[c:len(mascara)+c], mascara, True)
        vetor_resultante.append(prod_interno)
    print(vetor_resultante)
    return vetor_resultante


def main() -> None:
    '''
    Função que executa o programa.
    '''
    vetor_original = list(map(int, input().split(',')))
    entrada = ''
    while entrada != 'fim':
        entrada = input()

        if entrada == 'soma_vetores':
            vetor_2 = list(map(int, input().split(',')))
            vetor_original = soma_vetores(vetor_original, vetor_2)
        elif entrada == 'subtrai_vetores':
            vetor_2 = list(map(int, input().split(',')))
            vetor_original = subtrai_vetores(vetor_original, vetor_2)
        elif entrada == 'multiplica_vetores':
            vetor_2 = list(map(int, input().split(',')))
            vetor_original = multiplica_vetores(vetor_original, vetor_2)
        elif entrada == 'divide_vetores':
            vetor_2 = list(map(int, input().split(',')))
            vetor_original = divide_vetores(vetor_original, vetor_2)
        elif entrada == 'multiplicacao_escalar':
            escalar = int(input())
            vetor_original = multiplicacao_escalar(vetor_original, escalar)
        elif entrada == 'n_duplicacao':
            n = int(input())
            vetor_original = n_duplicacao(vetor_original, n)
        elif entrada == 'soma_elementos':
            vetor_original = [soma_elementos(vetor_original)]
        elif entrada == 'produto_interno':
            vetor_2 = list(map(int, input().split(',')))
            vetor_original = [produto_interno(vetor_original, vetor_2)]
        elif entrada == 'multiplica_todos':
            vetor_2 = list(map(int, input().split(',')))
            vetor_original = multiplica_todos(vetor_original, vetor_2)
        elif entrada == 'correlacao_cruzada':
            mascara = list(map(int, input().split(',')))
            vetor_original = correlacao_cruzada(vetor_original, mascara)


if __name__ == "__main__":
    main()
