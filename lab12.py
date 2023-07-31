class Carta:
    def __init__(self, carta) -> None:
        self._naipe = carta[-1]
        self._letra_ou_num = self.definir_letra_ou_num(carta)
        self._valor:str = self.definir_valor()
    @property
    def letra_ou_num(self):
        return self._letra_ou_num
    @property
    def naipe(self):
        return self._naipe
    @property
    def valor(self):
        return self._valor
    @property
    def valor_letra_ou_num(self):
        return self._valor_letra_ou_num

    def definir_letra_ou_num(self, carta):
        if carta[0] != '1':
            return carta[0]
        else:
            # Se o primeiro dígito da carta for 1:
            if len(carta) == 3:
                return '10'
            else:
                return '1'

    def definir_valor(self):
        '''Atribui uma string com três números a uma carta de acordo com seu
        número/letra e seu naipe. Os dois primeiros números correspondem à letra/numero, 
        indo de 01 até 13 (seguindo a ordem: A, 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, K).
        Já o terceiro número vai de 1 a 4 de acordo com o naipe (Na ordem: O, E, C, P)'''
        if self._letra_ou_num.isnumeric():
            if self._letra_ou_num != 10:
                primeiros_numeros = '0'+self._letra_ou_num
            else:
                primeiros_numeros = '10'
        else:
            if self._letra_ou_num == 'A':
                primeiros_numeros = '01'
            elif self._letra_ou_num == 'J':
                primeiros_numeros = '11'
            elif self._letra_ou_num == 'Q':
                primeiros_numeros = '12'
            elif self._letra_ou_num == 'K':
                primeiros_numeros = '13'
        self._valor_letra_ou_num = primeiros_numeros
        if self._naipe == 'O':
            terceiro_numero = 1
        elif self._naipe == 'E':
            terceiro_numero = 2
        elif self._naipe == 'C':
            terceiro_numero = 3
        elif self._naipe == 'P':
            terceiro_numero = 4
        return primeiros_numeros+str(terceiro_numero)

    
    def __str__(self) -> str:
        return self._letra_ou_num+self._naipe
    def __repr__(self) -> str:
        return self._letra_ou_num+self._naipe

def imprimir_pilha(pilha:list[Carta]):
    #Imprime a pilha
    cartas = [str(carta) for carta in pilha]
    if len(cartas) == 0:
        print('Pilha:')
    else:
        print(f'Pilha: {" ".join(cartas)}')

def imprimir_jogadores(jogadores:list[list[Carta]])->None:
    c = 1
    for jogador in jogadores:
        print(f'Jogador {c}')
        cartas = [str(carta) for carta in jogador]
        print(f'Mão: {" ".join(cartas)}')
        c += 1

def organizar_cartas(jogador:list[Carta]):
    # Organiza as cartas do jogador em ordem decrescente usando um algoritmo de selection sort
    for i in range(len(jogador)-1):
        maior = i
        for j in range(i+1, len(jogador)):
            if int(jogador[j].valor) > int(jogador[maior].valor):
                maior = j
        jogador[i], jogador[maior] = jogador[maior], jogador[i]
    return jogador
#def duvido():

def achar_numero_para_jogar(mao_do_jogador:list[Carta], ultima_carta:Carta)->str:
    # Retorna a letra ou numero que o jogador deve jogar
    inicio = 0
    fim = len(mao_do_jogador)-1
    while inicio <= fim:
        meio = (inicio+fim)//2
        if int(ultima_carta.valor_letra_ou_num) == int(mao_do_jogador[meio].valor_letra_ou_num):
            return ultima_carta.letra_ou_num
        elif int(ultima_carta.valor_letra_ou_num) > int(mao_do_jogador[meio].valor_letra_ou_num):
            fim = meio - 1
        else:
            inicio = meio + 1
    
    return mao_do_jogador[fim].letra_ou_num

def definir_valor(numero_ou_letra:str)->str:
    carta = Carta(numero_ou_letra+'O')
    return carta.valor_letra_ou_num


def definir_numero_de_cartas(jogador:list[Carta], tipo_da_carta:str):
    numero_de_cartas = 0
    for carta in jogador:
        if carta.letra_ou_num == tipo_da_carta:
            numero_de_cartas += 1
    return numero_de_cartas

def fazer_jogada(jogador_da_rodada:int, jogadores:list[list[Carta]], ultima_carta:Carta, pilha:list[Carta])->tuple[bool, list[Carta], list[list[Carta]]]:
    houve_blefe = False
    jogador = jogadores[jogador_da_rodada-1]
    numero_ou_letra = achar_numero_para_jogar(jogador, ultima_carta)
    n_cartas = definir_numero_de_cartas(jogador, numero_ou_letra)
    if ultima_carta.valor_letra_ou_num > definir_valor(numero_ou_letra):
        houve_blefe = True
    
    if not houve_blefe:
        print(f'[Jogador {jogador_da_rodada}] {n_cartas} carta(s) {numero_ou_letra}')
        ultima_carta = Carta(numero_ou_letra+'O')
    else:
        # Se houve blefe
        print(f'[Jogador {jogador_da_rodada}] {n_cartas} carta(s) {ultima_carta.letra_ou_num}')

    cartas_descartadas:list[Carta] = []
    for carta in jogador:
        if carta.letra_ou_num == numero_ou_letra:
            cartas_descartadas.append(carta)
    for carta in cartas_descartadas:
        jogador.remove(carta)
    cartas_descartadas = cartas_descartadas[::-1]
    for carta in cartas_descartadas:
        pilha.append(carta)
    imprimir_pilha(pilha)
    return (houve_blefe, pilha, jogadores, ultima_carta)


def main()->None:
    pilha:list[Carta] = []
    jogadores:list[list[Carta]] = []
    n_jogadores = int(input())
    for _ in range(n_jogadores):
        cartas = input().split(', ')
        jogadores.append([Carta(carta) for carta in cartas])
    n_jogadas = int(input())
    for jogador in jogadores:
        jogador = organizar_cartas(jogador)
    imprimir_jogadores(jogadores)
    imprimir_pilha(pilha)

    ha_vencedor = False
    ultima_carta:Carta = Carta('AO')
    contador_duvido = 0
    jogador_da_rodada = 1
    while not ha_vencedor:
        houve_blefe, pilha, jogadores, ultima_carta = fazer_jogada(jogador_da_rodada, jogadores, ultima_carta, pilha)

        if jogador_da_rodada == n_jogadores:
            jogador_da_rodada = 1
        jogador_da_rodada += 1
        contador_duvido += 1
        if contador_duvido == n_jogadas:
            print('Duvido')
            exit()
            contador_duvido = 0

main()


# IMPĹEMENTAR DUVIDO