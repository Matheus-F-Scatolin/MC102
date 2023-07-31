from typing import TypeVar
Monstro = TypeVar('Monstro')
Personagem = TypeVar('Personagem')


class Objeto:
    def __init__(self, nome:str, tipo_do_objeto:str, posicao:list[int], status:int, ja_foi_usado=False) -> None:
        self._nome = nome
        self._tipo_do_objeto = tipo_do_objeto
        self._posicao = posicao
        self._status = status
        self._ja_foi_usado = ja_foi_usado
    @property
    def nome(self)->str:
        return self._nome
    @property
    def tipo_do_objeto(self)->str:
        return self._tipo_do_objeto
    @property
    def posicao(self)->list[int]:
        return self._posicao
    @property
    def status(self)->int:
        return self._status
    @property
    def ja_foi_usado(self):
        return self._ja_foi_usado

    def aplicar_efeito(self, personagem)->None:
        '''
        Função que aplica os efeitos de um determinado objeto
        no personagem.

        Parâmetros:
            personagem (Personagem): O personagem.
        '''
        if self._tipo_do_objeto == 'v':
            # Se for um objeto de vida
            print(f'[v]Personagem adquiriu o objeto {self._nome} com status de {self._status}')
            personagem.mudar_vida(self._status)
            self._ja_foi_usado = True
        elif self._tipo_do_objeto == 'd':
            # Se for um objeto de dano
            print(f'[d]Personagem adquiriu o objeto {self._nome} com status de {self._status}')
            personagem.mudar_dano(self._status)
            self._ja_foi_usado = True


class Monstro:
    def __init__(self, vida:int, ataque:int, tipo_do_monstro:int, posicao:list[int]) -> None:
        self._vida = vida
        self._ataque = ataque
        self._tipo_do_monstro = tipo_do_monstro
        self._posicao = posicao
    @property
    def vida(self)->int:
        return self._vida
    @property
    def ataque(self)->int:
        return self._ataque
    @property
    def tipo_do_monstro(self)->str:
        return self._tipo_do_monstro
    @property
    def posicao(self)->list[int]:
        return self._posicao

    def andar(self, n_colunas:int, n_linhas:int, matriz:list[list[int]], objetos:list[object], monstros:list[Monstro], posicao_saida:list[int], link:Personagem)->list[list[int]]:
        '''
        Função que faz com que o personagem ande, e, após isso,
        retorna a matriz após a movimentação.
        
        Parâmetros:
            n_colunas (int): Número de colunas do mapa.
            n_linhas (int): Número de linhas do mapa.
            matriz (list[list[int]]): Matriz que representa a
            circunstância do ambiente em determinado momento.
            objetos (list[Object]): Lista com os objetos.
            monstros (list[Monstro]): Lista com os monstros.
            posicao_saida (list[int]): posicao da saída.
            link (Personagem): O personagem.

        
        Retorna:
            matriz (list[list[int]]): Matriz que representa a
            circunstância do ambiente após o movimento.
        '''
        posicao_original = self._posicao.copy()
        matriz[self._posicao[0]][self._posicao[1]] = '.'
        if self._tipo_do_monstro == 'U':
            # mover-se para cima
            if self._posicao[0] != 0:
                self._posicao[0] -= 1
        elif self._tipo_do_monstro == 'D':
            # mover-se para baixo
            if self._posicao[0] != n_linhas - 1:
                self._posicao[0] += 1
        elif self._tipo_do_monstro == 'L':
            # mover-se para a esquerda
            if self._posicao[1] != 0:
                self._posicao[1] -= 1
        elif self._tipo_do_monstro == 'R':
            #mover-se para a direita
            if self._posicao[1] != n_colunas - 1:
                self._posicao[1] += 1
        
        # testar se já havia alguma coisa na posicao original ou final do monstro
        if matriz[self._posicao[0]][self._posicao[1]] != '*':
            matriz[self._posicao[0]][self._posicao[1]] = self._tipo_do_monstro
        for objeto in objetos:
            if objeto.posicao == posicao_original:
                if not objeto.ja_foi_usado:
                    matriz[objeto.posicao[0]][objeto.posicao[1]] = objeto.tipo_do_objeto
        for monstro in monstros:
            if monstro.posicao == posicao_original:
                matriz[posicao_original[0]][posicao_original[1]] = monstro.tipo_do_monstro
            if monstro.posicao == self._posicao:
                matriz[self._posicao[0]][self._posicao[1]] = monstro.tipo_do_monstro
        if posicao_original == posicao_saida:
            matriz[posicao_saida[0]][posicao_saida[1]] = '*'
        elif self._posicao == posicao_saida:
            matriz[posicao_saida[0]][posicao_saida[1]] = '*'
        if posicao_original == link.posicao:
            matriz[posicao_original[0]][posicao_original[1]] = 'P'
        elif self._posicao == link.posicao:
            matriz[self._posicao[0]][self._posicao[1]] = 'P'
        return matriz
    
    def receber_dano(self, dano_recebido:int)->bool:
        if dano_recebido > self._vida:
            dano_recebido = self._vida
        print(f'O Personagem deu {dano_recebido} de dano ao monstro na posicao {tuple(self._posicao)}')
        self._vida -= dano_recebido
        if self._vida == 0:
            return False
        else:
            return True


class Personagem:
    def __init__(self, vida:int, dano:int, posicao:list[int]) -> None:
        self._vida = vida
        self._dano = dano
        self._posicao = posicao
    @property
    def vida(self):
        return self._vida
    @property
    def dano(self):
        return self._dano
    @property
    def posicao(self):
        return self._posicao
    def andar_personagem(self, matriz:list[list[str]], direcao:str)->list[list[str]]:
        '''
        Função que faz com que o personagem ande 1 posição.

        Parâmetros:
            matriz (list[list[str]]): uma matriz que inclui a situação momentânea do 
            ambiente.
            direcao (str): A direção desejada.

        Retorna:
            matriz: a matriz após o movimento.
        '''
        matriz[self._posicao[0]][self._posicao[1]] = '.'
        if direcao == 'direita':
            self._posicao[1] += 1
        elif direcao == 'esquerda':
            self._posicao[1] -= 1
        elif direcao == 'cima':
            self._posicao[0] -= 1
        elif direcao == 'baixo':
            self._posicao[0] += 1
        matriz[self._posicao[0]][self._posicao[1]] = 'P'
        return matriz
    
    def mudar_vida(self, variacao_da_vida:int)->None:
        '''
        Função que muda a vida do personagem.
        
        Parâmetros:
            variacao_da_vida (int): A variação da vida (pode receber valores positivos
            ou negativos)
        '''
        self._vida += variacao_da_vida
        if self._vida < 0:
            self._vida = 0
    
    def mudar_dano(self, variacao_do_dano:int)->None:
        '''
        Função que muda o dano do personagem.
        
        Parâmetros:
            variacao_do_dano (int): A variação do dano (pode receber valores positivos
            ou negativos)
        '''
        self._dano += variacao_do_dano
        if self._dano < 1:
            self._dano = 1
    
    def receber_dano(self, dano_recebido:int)->None:
        '''
        Função que faz com que o personagem receba dano.
        
        Parâmetros:
            dano_recebido (int): O dano a ser recebido (positivo).
        '''
        if dano_recebido > self._vida:
            dano_recebido = self._vida
        self.mudar_vida(-dano_recebido)
        print(f'O Monstro deu {dano_recebido} de dano ao Personagem. Vida restante = {self._vida}')
    
    def testar_direcao(self, n_colunas:int)->str:
        '''
        Função que testa a direção para qual o personagem deve se
        movimentar.
        
        Parâmetros:
            n_colunas (int): O número de colunas do mapa.
        Retorna:
            (str): A direção correta para o Personagem.
        '''
        if self._posicao[0] % 2 == 0:
            # Se link estiver em uma linha par, mover-se para a a esquerda
                if self._posicao[1] != 0:
                    return 'esquerda'
                else:
                    return 'cima'
        else:
            # Se link estiver em uma linha ímpar, mover-se para a a direita
            if self._posicao[1] != n_colunas - 1:
                return 'direita'
            else:
                return 'cima'


def ler_monstro(linha_de_texto:str) -> Monstro:
    '''
    Função que lê uma linha e cria um monstro com base nas
    informações da linha.
    
    Parâmetros:
        linha_de_texto (str): A linha de texto com as informações.
    Retorna:
        (Monstro): O monstro com os atributos da linha de texto.
    '''
    vida, ataque, tipo_do_monstro, coordenadas = linha_de_texto.split()
    # corrigir a formatação da posicao
    posicao = list(map(int,coordenadas.split(',')))
    return Monstro(int(vida), int(ataque), tipo_do_monstro, posicao)


def ler_objeto(linha_de_texto:str) -> Objeto:
    '''
    Função que lê uma linha e cria um objeto com base nas
    informações da linha.
    
    Parâmetros:
        linha_de_texto (str): A linha de texto com as informações.
    Retorna:
        (Objeto): O objeto com os atributos da linha de texto.
    '''
    nome, tipo, coordenadas, status = linha_de_texto.split()
    # corrigir a formatação da posicao
    posicao = list(map(int,coordenadas.split(',')))
    return Objeto(nome, tipo, posicao, int(status))


def mostrar_matriz(matriz:list[list[int]]) -> None:
    '''
    Função que imprime a matriz

    Parâmetros:
        matriz (list[list[str]]): uma matriz que inclui a situação momentânea do 
        ambiente.
    '''
    for linha in matriz:
        print(" ".join(linha))


def testar_encontros(personagem:Personagem, objetos:list[Objeto], monstros:list[Monstro]) -> list[list[Objeto], list[Monstro]]:
    '''
    Função que testa os encontros que ocorreram em determinada circunstância
    do mapa.
    
    Parâmetros:
        personagem (Personagem): O personagem.
        objetos (list[Objeto]): Lista com os objetos do mapa.
        monstros (list[Monstro]): Lista com os monstros do mapa.
    Retorna:
        encontros (list[list[Objeto], list[Monstro]]): Lista com os encontros
        que ocorreram.
    '''
    encontros:list[list[Objeto], list[Monstro]] = [[], []]
    posicao_personagem = personagem.posicao
    for objeto in objetos:
        if objeto.posicao == posicao_personagem and not objeto.ja_foi_usado:
            encontros[0].append(objeto)
    for monstro in monstros:
        if monstro.posicao == posicao_personagem:
            encontros[1].append(monstro)
    return encontros


def combate(personagem:Personagem, monstros:list[Monstro],monstros_combate:list[Monstro]) -> None:
    '''
    Função que é responsável pela execução dos combates
    entre o personagem e um ou mais monstros.
    
    Parâmetros:
        personagem (Personagem): O personagem.
        monstros (list[Monstro]): Lista todos com os monstros do mapa.
        monstros_combate (list[Monstro]): Lista com os monstros envolvidos
        no combate.
    '''
    for monstro in monstros:
        if monstro in monstros_combate:
            if personagem.vida != 0:
                monstro_vivo = monstro.receber_dano(personagem.dano)
            if monstro_vivo and personagem.vida != 0:
                personagem.receber_dano(monstro.ataque)
            elif not monstro_vivo:
                monstros.remove(monstro)


def main() -> None:
    vida_inicial, dano_inicial = input().split()
    n_linhas, n_colunas = list(map(int, input().split()))
    matriz = [['.' for i in range (n_colunas)] for j in range (n_linhas)]
    ix, iy = input().split(',')
    posicao_inicial = [int(ix), int(iy)]
    link = Personagem(int(vida_inicial), int(dano_inicial), posicao_inicial)
    fx, fy = input().split(',')
    posicao_saida = [int(fx), int(fy)]

    n_montros = int(input())
    monstros:list[Monstro] = []
    for c in range (n_montros):
        monstro = ler_monstro(input())
        monstros.append(monstro)

    n_objetos = int(input())
    objetos:list[Objeto] = []
    for c in range (n_objetos):
        objeto = ler_objeto(input())
        objetos.append(objeto)

    # posicionar cada elemento na matriz
    for objeto in objetos:
        matriz[objeto.posicao[0]][objeto.posicao[1]] = objeto.tipo_do_objeto
    for monstro in monstros:
        matriz[monstro.posicao[0]][monstro.posicao[1]] = monstro.tipo_do_monstro
    matriz[posicao_saida[0]][posicao_saida[1]] = '*'
    matriz[link.posicao[0]][link.posicao[1]] = 'P'
    mostrar_matriz(matriz)
    print()

    iniciar_movimentacao = True
    while link.posicao != posicao_saida:
        if iniciar_movimentacao:
            if link.posicao[0] != n_linhas-1:
                matriz = link.andar_personagem(matriz, 'baixo')
            else:
                iniciar_movimentacao = False
                matriz = link.andar_personagem(matriz, link.testar_direcao(n_colunas))
        else:
            matriz = link.andar_personagem(matriz, link.testar_direcao(n_colunas))

        # Testar se ele chegou na saida com a última movimentação
        if link.posicao == posicao_saida:
            mostrar_matriz(matriz)
            print()
            break

        #atualizar a posicao dos monstros
        for monstro in monstros:
            matriz = monstro.andar(n_colunas, n_linhas, matriz, objetos, monstros, posicao_saida, link)

        #testar se link se encontrou com algum monstro ou item
        encontros:list[list[Objeto], list[Monstro]] = testar_encontros(link, objetos, monstros)
        if encontros != [[], []]:
            # Se tiver ocorrido algum encontro
            if encontros[0] != []:
                # aplicar o efeito dos items
                for item in encontros[0]:
                    item.aplicar_efeito(link)
            if encontros[1] != []:
                combate(link, monstros, encontros[1])
        
        if link.vida == 0:
            # Se Link tiver morrido
            matriz[link.posicao[0]][link.posicao[1]] = 'X'
            mostrar_matriz(matriz)
            exit()

        mostrar_matriz(matriz)
        print()

    print('Chegou ao fim!')


main()
