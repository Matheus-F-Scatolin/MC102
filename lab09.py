def mostrar_matriz(matriz:list[list[int]]) -> None:
    '''
    Função que fimprime a matriz

    Parâmetros:
        matriz (list[list[str]]): uma matriz que inclui a situação momentânea do 
        ambiente.
    '''
    for linha in matriz:
        print(" ".join(linha))


def limpando(matriz:list[list[str]], posicao_robo:list[int], vizinhanca:list[str]) -> list[list[list[str]], list[int]]:
    '''
    Função que faz com que o robô limpe as casas adequadas. Dentro de sua lógica, 
    ela inclui recursões para que o robô só pare de limpar quando todas as casas 
    em sua vizinhança estejam limpas.

    Parâmetros:
        matriz (list[list[str]]): uma matriz que inclui a situação momentânea do 
        ambiente.
        posicao_robo (list[int]): uma lista com a posicao do robo.
        vizinhanca (list[str]): uma lista com a vizinhança do robo.

    Retorna:
        matriz: a matriz após as mudanças serem feitas.
        posicao_robo: a posicao do robo após a limpeza.
    '''
    global posicao_original
    global caminho_certo
    matriz_original = [linha.copy() for linha in matriz]
    posicao_robo_original = posicao_robo.copy()

    sujeira = vizinhanca.index('o')
    if sujeira == 0:
        # Limpar na esquerda
        matriz, posicao_robo = andar_robo(matriz, posicao_robo, 'esquerda')
    elif sujeira == 1:
        # Limpar em cima
        matriz, posicao_robo = andar_robo(matriz, posicao_robo, 'cima')
    elif sujeira == 2:
        # Limpar na direita
        matriz, posicao_robo = andar_robo(matriz, posicao_robo, 'direita')
    elif sujeira == 3:
        # Limpar em baixo
        matriz, posicao_robo = andar_robo(matriz, posicao_robo, 'baixo')
    
    if caminho_certo:
        if testar_caminho(matriz_original, posicao_robo_original) == posicao_robo:
            posicao_original = posicao_robo.copy()
        else:
            caminho_certo = False

    if 'o' in escanear_posicao(matriz, posicao_robo):
        limpando(matriz, posicao_robo, escanear_posicao(matriz, posicao_robo))
    return [matriz, posicao_robo]


def testar_caminho(matriz_original:list[list[str]], posicao_robo) -> list[int]:
    '''
    Função que testa se a primeira sujeira ja estava no caminho original do robo, 
    e retorna a posicao original correta.

    Parâmetros:
        matriz_original (list[list[str]]): uma matriz que inclui a situação momentânea do 
        ambiente.
        posicao_robo (list[int]): uma lista com a posicao do robo.

    Retorna:
        posicao_robo: a posicao correta para a volta do robô.
    '''
    # Testa se a primeira sujeira ja estava no caminho original do robo, e retorna a posicao original correta
    if posicao_robo[0]%2 == 0:
        if posicao_robo[1] != len(matriz_original[0]) -1:
            if matriz_original[posicao_robo[0]][posicao_robo[1]+1] == 'o':
                return [posicao_robo[0], posicao_robo[1]+1]
        else:
            if matriz_original[posicao_robo[0]+1][posicao_robo[1]] == 'o':
                return [posicao_robo[0]+1,posicao_robo[1]]

    elif posicao_robo[0]%2 != 0:
        if posicao_robo[1] == 0:
            if matriz_original[posicao_robo[0]+1][posicao_robo[1]] == 'o':
                return [posicao_robo[0]+1, posicao_robo[1]]
        else:
            if matriz_original[posicao_robo[0]][posicao_robo[1]-1] == 'o':
                return [posicao_robo[0], posicao_robo[1]-1]

    return posicao_robo.copy()

def retornar_escaneamento(matriz:list[list[str]], posicao_robo, posicao_original) -> list[list[list[str]], list[int]]:
    '''
    Função que faz com que o robô retorne à sua posição inicial.

    Parâmetros:
        matriz (list[list[str]]): uma matriz que inclui a situação momentânea do 
        ambiente.
        posicao_robo (list[int]): uma lista com a posicao do robo.
        posicao_original (list[int]): uma lista com a posicao desejada para o robo.

    Retorna:
        matriz: a matriz após as mudanças serem feitas.
        posicao_robo: a posicao do robo após o retorno.
    '''
    if posicao_robo[0]%2 == 0:
        if (posicao_robo[1] == posicao_original[1] + 1) and posicao_robo[0] == posicao_original[0]:
            return matriz, posicao_robo
    elif posicao_robo[0]%2 != 0:
        if (posicao_robo[1] == posicao_original[1] - 1) and posicao_robo[0] == posicao_original[0]:
            return matriz, posicao_robo
    if (posicao_robo[1] == 0) and posicao_robo[0] % 2 == 0:
        if (posicao_robo[0] == posicao_original[0] + 1) and posicao_robo[1] == posicao_original[1]:
            return matriz, posicao_robo
    elif (posicao_robo[1] == len(matriz[0])-1) and posicao_robo[0] % 2 != 0:
        if (posicao_robo[0] == posicao_original[0] + 1) and posicao_robo[1] == posicao_original[1]:
            return matriz, posicao_robo

    # Caso contrario, voltar até a coluna original e, depois, até a linha original
    while posicao_robo[1] != posicao_original[1]:
        if posicao_robo[1] < posicao_original[1]:
            matriz, posicao_robo = andar_robo(matriz, posicao_robo, 'direita')
            # Testar se há novas sujeiras no caminho
            if 'o' in escanear_posicao(matriz, posicao_robo):
                limpando(matriz, posicao_robo, escanear_posicao(matriz, posicao_robo))
        else:
            matriz, posicao_robo = andar_robo(matriz, posicao_robo, 'esquerda')
            if 'o' in escanear_posicao(matriz, posicao_robo):
                limpando(matriz, posicao_robo, escanear_posicao(matriz, posicao_robo))

    while posicao_robo[0] != posicao_original[0]:
        if posicao_robo[0] < posicao_original[0]:
            matriz, posicao_robo = andar_robo(matriz, posicao_robo, 'baixo')
            if 'o' in escanear_posicao(matriz, posicao_robo):
                limpando(matriz, posicao_robo, escanear_posicao(matriz, posicao_robo))
        else:
            matriz, posicao_robo = andar_robo(matriz, posicao_robo, 'cima')
            if 'o' in escanear_posicao(matriz, posicao_robo):
                limpando(matriz, posicao_robo, escanear_posicao(matriz, posicao_robo))
    
    return [matriz, posicao_robo]


def andar_robo(matriz:list[list[str]], posicao_robo, direcao)  -> list[list[list[str]], list[int]]:
    '''
    Função que faz com que o robô ande 1 posição.

    Parâmetros:
        matriz (list[list[str]]): uma matriz que inclui a situação momentânea do 
        ambiente.
        posicao_robo (list[int]): uma lista com a posicao do robo.
        direcao (str): A direção desejada.

    Retorna:
        matriz: a matriz após o movimento.
        posicao_robo: a posicao do robo após o movimento.
    '''
    matriz[posicao_robo[0]][posicao_robo[1]] = '.'
    if direcao == 'direita':
        posicao_robo[1] += 1
    elif direcao == 'esquerda':
        posicao_robo[1] -= 1
    elif direcao == 'cima':
        posicao_robo[0] -= 1
    elif direcao == 'baixo':
        posicao_robo[0] += 1
    matriz[posicao_robo[0]][posicao_robo[1]] = 'r'
    mostrar_matriz(matriz)
    print()
    return [matriz, posicao_robo]



def escanear_posicao(matriz:list[list[str]], posicao_robo) -> list[str]:
    '''
    Função que escaneia a vizinhança do robo.

    Parâmetros:
        matriz (list[list[str]]): uma matriz que inclui a situação momentânea do 
        ambiente.
        posicao_robo (list[int]): uma lista com a posicao do robo.

    Retorna:
        vizinhanca: uma lista com a vizinhança do robô.
    '''
    # [esquerda, cima, direita, baixo]
    # esquerda
    vizinhanca = []
    if posicao_robo[1] == 0:
        vizinhanca.append('.')
    else:
        vizinhanca.append(matriz[posicao_robo[0]][posicao_robo[1]-1])
    # cima
    if posicao_robo[0] == 0:
        vizinhanca.append('.')
    else:
        vizinhanca.append(matriz[posicao_robo[0]-1][posicao_robo[1]])
    # direita
    if posicao_robo[1] == len(matriz[0])-1:
        vizinhanca.append('.')
    else:
        vizinhanca.append(matriz[posicao_robo[0]][posicao_robo[1]+1])
    # baixo
    if posicao_robo[0] == len(matriz)-1:
        vizinhanca.append('.')
    else:
        vizinhanca.append(matriz[posicao_robo[0]+1][posicao_robo[1]])
    return vizinhanca
    

def main() -> None:
    n_linhas = int(input())
    matriz = [[x for x in input().split()] for _ in range (n_linhas)]
    n_colunas = len(matriz[0])
    posicao_robo = [0, 0]
    global posicao_original
    posicao_original = [0, 0]
    modo = 0
    # modo 0: escaneamento, modo 1: limpando, modo 2:retornar ao escaneamento
    mostrar_matriz(matriz)
    print()
    funcionando = True
    global caminho_certo
    caminho_certo = True
    while funcionando:
        caminho_certo = True
        modo = 0

        if 'o' in escanear_posicao(matriz, posicao_robo):
            modo = 1
        
        if modo == 0:
            if posicao_robo[0] % 2 == 0:
                # se o robo estiver em uma linha par, andar para a direita
                if posicao_robo[1] != n_colunas - 1:
                    matriz, posicao_robo = andar_robo(matriz, posicao_robo, direcao='direita')
                else:
                    matriz, posicao_robo = andar_robo(matriz, posicao_robo, direcao='baixo')
            else:
                # Se o robo estiver em uma linha ímpar, andar para a esquerda
                if posicao_robo[1] != 0:
                    matriz, posicao_robo = andar_robo(matriz, posicao_robo, direcao='esquerda')
                else:
                    matriz, posicao_robo = andar_robo(matriz, posicao_robo, direcao='baixo')

        elif modo == 1:
            posicao_original = testar_caminho(matriz, posicao_robo)
            matriz, posicao_robo = limpando(matriz, posicao_robo, escanear_posicao(matriz, posicao_robo))
            modo = 2
        
        if modo == 2:
            matriz, posicao_robo = retornar_escaneamento(matriz, posicao_robo, posicao_original)
        
        if len(matriz) % 2 != 0:
            if posicao_robo == [len(matriz)-1, len(matriz[0])-1]:
                funcionando = False
        else:
            # Se existir um número par de linhas
            if modo == 0 and posicao_robo == [len(matriz)-1, 0]:
                for c in range(len(matriz[0])-1):
                    matriz, posicao_robo = andar_robo(matriz, posicao_robo, 'direita')
                funcionando = False

main()
