import sys
sys.setrecursionlimit(163850)

def ler_operacao(linha_de_texto:str)->tuple[str, int, int, tuple[int]]:
    """
    Lê uma linha de texto contendo uma operação e seus parâmetros e retorna uma tupla com as informações da operação.

    Parâmetros:
    - linha_de_texto (str): Uma linha de texto contendo a operação e seus parâmetros separados por espaços.

    Retorno:
    - Tupla contendo as informações da operação: (operacao, cor_preenchimento, limiar, coordenada)
    """
    informacoes = linha_de_texto.split()
    cor_preenchimento = None
    if informacoes[0] == 'bucket':
        operacao = informacoes[0]
        cor_preenchimento = int(informacoes[1])
        limiar = int(informacoes[2])
        coordenada = (int(informacoes[4]), int(informacoes[3]))
    else:
        operacao = informacoes[0]
        limiar = int(informacoes[1])
        coordenada = (int(informacoes[3]), int(informacoes[2]))
    if operacao == 'bucket':
        return (operacao, cor_preenchimento, limiar, coordenada)
    else:
        return (operacao, limiar, coordenada)   


def pintar_casa(matriz:list[list[int]], cor_preenchimento:int, coordenada_a_ser_pintada:tuple[int],
                posicoes_pintadas:set[tuple[int]])->tuple[list[list[int]], list[tuple[int]]]:
    """
    Pinta uma casa na matriz com uma determinada cor de preenchimento e adiciona sua posição à lista de posições pintadas.

    Parâmetros:
    - matriz (list[list[int]]): A matriz de pixels.
    - cor_preenchimento (int): A cor de preenchimento a ser aplicada na casa.
    - coordenada_a_ser_pintada (tuple[int]): As coordenadas da casa a ser pintada.
    - posicoes_pintadas (list[tuple[int]]): Lista de posições já pintadas.

    Retorno:
    - Tupla contendo a matriz atualizada e a lista de posições pintadas: (matriz, posicoes_pintadas)
    """
    matriz[coordenada_a_ser_pintada[0]][coordenada_a_ser_pintada[1]] = cor_preenchimento
    posicoes_pintadas.add((coordenada_a_ser_pintada[0], coordenada_a_ser_pintada[1]))
    return (matriz, posicoes_pintadas)


def analisar_vizinhanca(matriz:list[list[int]], cor_preenchimento:int, cor_semente:int,
                        limiar:int, coordenada:tuple[int], posicoes_pintadas:set[tuple[int]],
                        vizinhanca:list[tuple[int]])->tuple[list[list[int]], list[tuple[int]], list[tuple[int]]]:
    """
    Analisa a vizinhança de uma casa para identificar outras casas que devem ser pintadas com base em determinados critérios.

    Parâmetros:
    - matriz (list[list[int]]): A matriz de pixels.
    - cor_preenchimento (int|None): A cor de preenchimento a ser aplicada nas casas da vizinhança (ou None se não houver cor de preenchimento).
    - cor_semente (int): A cor da casa semente.
    - limiar (int): O limiar de diferença de cores para decidir se uma casa será pintada.
    - coordenada (tuple[int]): As coordenadas da casa semente.
    - posicoes_pintadas (list[tuple[int]]): Lista de posições já pintadas.
    - vizinhanca (list[tuple[int]]): Lista de vizinhos encontrados até o momento.

    Retorno:
    - Lista de vizinhos atualizada: vizinhanca
    """
    n_linhas = len(matriz)
    n_colunas = len(matriz[0])
    if coordenada[0] != n_linhas - 1:
        #testar a casas abaixo da casa atual
        cor = matriz[coordenada[0]+1][coordenada[1]]
        if abs(cor - cor_semente) <= limiar and (coordenada[0]+1, coordenada[1]) not in posicoes_pintadas and \
        (cor_semente != cor_preenchimento or cor_preenchimento == None):
            vizinhanca.add((coordenada[0]+1, coordenada[1]))
        if coordenada[1] != 0:
            # testar a casa na diagonal esquerda inferior
            cor = matriz[coordenada[0]+1][coordenada[1]-1]
            if abs(cor - cor_semente) <= limiar and (coordenada[0]+1, coordenada[1]-1) not in posicoes_pintadas and \
        (cor_semente != cor_preenchimento or cor_preenchimento == None):
                vizinhanca.add((coordenada[0]+1, coordenada[1]-1))
        if coordenada[1] != n_colunas - 1:
            # Testar a casa na diagonal inferior direita
            cor = matriz[coordenada[0]+1][coordenada[1]+1]
            if abs(cor - cor_semente) <= limiar and (coordenada[0]+1, coordenada[1]+1) not in posicoes_pintadas and \
        (cor_semente != cor_preenchimento or cor_preenchimento == None):
                vizinhanca.add((coordenada[0]+1, coordenada[1]+1))
    
    if coordenada[0] != 0:
        #testar as casas acima da atual
        cor = matriz[coordenada[0]-1][coordenada[1]]
        if abs(cor - cor_semente) <= limiar and (coordenada[0]-1, coordenada[1]) not in posicoes_pintadas and \
        (cor_semente != cor_preenchimento or cor_preenchimento == None):
            vizinhanca.add((coordenada[0]-1, coordenada[1]))
        if coordenada[1] != 0:
            # testar a casa na diagonal esquerda superior
            cor = matriz[coordenada[0]-1][coordenada[1]-1]
            if abs(cor - cor_semente) <= limiar and (coordenada[0]-1, coordenada[1]-1) not in posicoes_pintadas and \
        (cor_semente != cor_preenchimento or cor_preenchimento == None):
                vizinhanca.add((coordenada[0]-1, coordenada[1]-1))
        if coordenada[1] != n_colunas - 1:
            # Testar a casa na diagonal superior direita
            cor = matriz[coordenada[0]-1][coordenada[1]+1]
            if abs(cor - cor_semente) <= limiar and (coordenada[0]-1, coordenada[1]+1) not in posicoes_pintadas and \
        (cor_semente != cor_preenchimento or cor_preenchimento == None):
                vizinhanca.add((coordenada[0]-1, coordenada[1]+1))
    
    # testar a casa à direita da atual
    if coordenada[1] != n_colunas - 1:
        cor = matriz[coordenada[0]][coordenada[1]+1]
        if abs(cor - cor_semente) <= limiar and (coordenada[0], coordenada[1]+1) not in posicoes_pintadas and \
        (cor_semente != cor_preenchimento or cor_preenchimento == None):
            vizinhanca.add((coordenada[0], coordenada[1]+1))

    #testar à esquerda da casa atual
    if coordenada[1] != 0:
        cor = matriz[coordenada[0]][coordenada[1]-1]
        if abs(cor - cor_semente) <= limiar and (coordenada[0], coordenada[1]-1) not in posicoes_pintadas and \
        (cor_semente != cor_preenchimento or cor_preenchimento == None):
            vizinhanca.add((coordenada[0], coordenada[1]-1))
    
    return vizinhanca


def bucket(matriz:list[list[int]], cor_preenchimento:int, limiar:int, coordenada:tuple[int],
           posicoes_pintadas:set[tuple[int]], vizinhanca:list[tuple[int]], cor_semente:int)->tuple[list[list[int]],
           list[tuple[int]], list[tuple[int]]]:
    """
    Implementa a operação de "bucket" para preenchimento de uma área da matriz com uma determinada cor.

    Parâmetros:
    - matriz (list[list[int]]): A matriz de pixels.
    - cor_preenchimento (int): A cor de preenchimento a ser aplicada nas casas da área.
    - limiar (int): O limiar de diferença de cores para decidir se uma casa será pintada.
    - coordenada (tuple[int]): As coordenadas iniciais da área a ser preenchida.
    - posicoes_pintadas (list[tuple[int]]): Lista de posições já pintadas.
    - vizinhanca (list[tuple[int]]): Lista de vizinhos encontrados até o momento.

    Retorno:
    - Matriz atualizada após o preenchimento da área: matriz
    """
    #cor_semente = matriz[coordenada[0]][coordenada[1]]
    # pintar a coordenada e adicioná-la à lista de posicoes pintadas
    matriz, posicoes_pintadas = pintar_casa(matriz, cor_preenchimento, (coordenada[0], coordenada[1]), posicoes_pintadas)
    # Adicionar à vizinhança todas as coordenadas proximas à coordenada inicial que devem ser pintadas
    vizinhanca = analisar_vizinhanca(matriz, cor_preenchimento, cor_semente, limiar, coordenada, posicoes_pintadas, vizinhanca)
    # Percorrer a vizinhança, pintando todas as suas casas, e, no processo, adicionar mais casas à vizinhança
    for casa_vizinha in vizinhanca.copy():
        if casa_vizinha not in posicoes_pintadas:
            matriz, posicoes_pintadas, vizinhanca = bucket(matriz, cor_preenchimento, limiar, casa_vizinha, posicoes_pintadas, vizinhanca, cor_semente)
    return (matriz, posicoes_pintadas, vizinhanca)


def negative(matriz:list[list[int]], limiar:int, coordenada:tuple[int], posicoes_pintadas:set[tuple[int]],
             vizinhanca:list[tuple[int]], cor_semente:int)->tuple[list[list[int]], list[tuple[int]], list[tuple[int]]]:
    """
    Implementa a operação de "negativo" para inverter as cores de uma área da matriz.

    Parâmetros:
    - matriz (list[list[int]]): A matriz de pixels.
    - coordenada (tuple[int]): As coordenadas iniciais da área a ser invertida.
    - posicoes_pintadas (list[tuple[int]]): Lista de posições já pintadas.

    Retorno:
    - Matriz atualizada após a operação de negativo: matriz
    """
    #cor_semente = matriz[coordenada[0]][coordenada[1]]
    # pintar a coordenada e adicioná-la à lista de posicoes pintadas
    cor_atual = matriz[coordenada[0]][coordenada[1]]
    matriz, posicoes_pintadas = pintar_casa(matriz, 255-cor_atual , (coordenada[0], coordenada[1]), posicoes_pintadas)
    vizinhanca = analisar_vizinhanca(matriz, None, cor_semente, limiar, coordenada, posicoes_pintadas, vizinhanca)
    # Percorrer a vizinhança, pintando todas as suas casas, e, no processo, adicionar mais casas à vizinhança
    for casa_vizinha in vizinhanca.copy():
        if casa_vizinha not in posicoes_pintadas:
            matriz, posicoes_pintadas, vizinhanca = negative(matriz, limiar, casa_vizinha, posicoes_pintadas, vizinhanca, cor_semente)
    return (matriz, posicoes_pintadas, vizinhanca)


def mascara(matriz:list[list[int]], limiar:int, coordenada:tuple[int], posicoes_pintadas:set[tuple[int]],
            vizinhanca:list[tuple[int]], cor_semente:int)->tuple[list[list[int]], list[tuple[int]], list[tuple[int]]]:
    """
    Implementa a operação de "máscara" para aplicar uma máscara a uma área da matriz.

    Parâmetros:
    - matriz (list[list[int]]): A matriz de pixels.
    - mascara (list[list[int]]): A máscara a ser aplicada.
    - coordenada (tuple[int]): As coordenadas iniciais da área a ser mascarada.
    - posicoes_pintadas (list[tuple[int]]): Lista de posições já pintadas.

    Retorno:
    - Matriz atualizada após a aplicação da máscara: matriz
    """
    #cor_semente = matriz[coordenada[0]][coordenada[1]]
    # adicionar a coordenada atual à lista de posicoes pintadas e pintá-la
    matriz, posicoes_pintadas = pintar_casa(matriz, 0, (coordenada[0], coordenada[1]), posicoes_pintadas)
    vizinhanca = analisar_vizinhanca(matriz, None, cor_semente, limiar, coordenada, posicoes_pintadas, vizinhanca)
    # Percorrer a vizinhança, pintando todas as suas casas, e, no processo, adicionar mais casas à vizinhança
    for casa_vizinha in vizinhanca.copy():
        if casa_vizinha not in posicoes_pintadas:
            matriz, posicoes_pintadas, vizinhanca = mascara(matriz, limiar, casa_vizinha, posicoes_pintadas, vizinhanca, cor_semente)

    # Após todas as recursões, pintar de branco as casas não selecionadas
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if (i, j) not in posicoes_pintadas:
                matriz[i][j] = 255

    return (matriz, posicoes_pintadas, vizinhanca)


def executar_operacao(matriz:list[list[int]], operacao:str, cor_preenchimento:int, limiar:int,
                      coordenada:tuple[int])->list[list[int]]:
    """
    Recebe uma operação, seus argumentos e a matriz atual, e executa a operação correspondente na matriz.

    Parâmetros:
    - operacao (str): A operação a ser executada.
    - argumentos (tuple[int|None, int, tuple[int]]): Os argumentos da operação.
    - matriz (list[list[int]]): A matriz de pixels.

    Retorno:
    - Matriz atualizada após a execução da operação: matriz
    """
    vizinhanca = set()
    posicoes_pintadas = set()
    cor_semente = matriz[coordenada[0]][coordenada[1]]
    if operacao == 'bucket':
        matriz, posicoes_pintadas, vizinhanca = bucket(matriz, cor_preenchimento, limiar, coordenada, posicoes_pintadas, vizinhanca, cor_semente)
    elif operacao == 'negative':
        matriz, posicoes_pintadas, vizinhanca = negative(matriz, limiar, coordenada, posicoes_pintadas, vizinhanca, cor_semente)
    elif operacao == 'cmask':
        matriz, posicoes_pintadas, vizinhanca = mascara(matriz, limiar, coordenada, posicoes_pintadas, vizinhanca, cor_semente)
    return matriz


def main()->None:
    path_arquivo = input()
    with open(path_arquivo) as arquivo:
        linhas = arquivo.readlines()[4:]
        matriz = ([list(map(int, linha.strip().split())) for linha in linhas if linha != '\n'])
    
    n_operacoes = int(input())
    for _ in range(n_operacoes):
        linha_de_input = input()
        if linha_de_input.split()[0] != 'save':
            if linha_de_input.split()[0] == 'bucket':
                operacao, cor_preenchimento, limiar, coordenada = ler_operacao(linha_de_input)
                matriz = executar_operacao(matriz, operacao, cor_preenchimento, limiar, coordenada)
            else:
                operacao, limiar, coordenada = ler_operacao(linha_de_input)
                matriz = executar_operacao(matriz, operacao, None, limiar, coordenada)
        else:
            # Se o programa deve salvar a imagem
            '''caminho_saida = linha_de_input.split()[1]
            with open(caminho_saida, "w") as arquivo_saida:
                arquivo_saida.write(f'P2\n# Imagem criada pelo lab13\n{len(matriz[0])} {len(matriz)}\n255\n')
                for linha in matriz:
                    linha_formatada = " ".join(str(elemento) for elemento in linha)
                    arquivo_saida.write(linha_formatada + "\n")'''
            print('P2\n# Imagem criada pelo lab13\n' + str(len(matriz[0])), len(matriz))
            print('255')
            for linha in matriz:
                print(" ".join(str(elemento) for elemento in linha))

main()