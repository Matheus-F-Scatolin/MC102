class Aloy:
    def __init__(self, vida:int, flechas:dict[str:int]):
        self._vida_maxima = vida
        self._vida = vida
        self._flechas = flechas

    @property
    def vida(self):
        return self._vida
    @property
    def flechas(self):
        return self._flechas

    def ler_vida(self)->int:
        '''
        Função que lê a vida atual de Aloy.
        '''
        return self._vida
    
    def ler_num_flecha(self, tipo_da_flecha:str)->int:
        '''
        Função que lê o número de flechas de determinado tipo.
        '''
        return self._flechas[tipo_da_flecha]

    def curar(self)->None:
        '''
        Função que cura Aloy após o início de cada combate.
        '''
        vida_final = self._vida + self._vida_maxima//2
        if vida_final > self._vida_maxima:
            self._vida = self._vida_maxima
        else:
            self._vida = vida_final
    def receber_dano(self, dano_recebido:int)->None:
        '''
        Função que faz com que Aloy receba dano.
        '''
        if self._vida - dano_recebido <= 0:
            self._vida = 0
        else:
            self._vida = self._vida - dano_recebido

class Monstro:
    def __init__(self, pontos_de_vida:int, pontos_de_ataque:int, quantidade_de_partes:int, partes=None):
        self._pontos_de_vida = pontos_de_vida
        self._pontos_de_ataque = pontos_de_ataque
        self._quantidade_de_partes = quantidade_de_partes
        if partes == None:
            self._partes = []
        else:
            self._partes = self.partes.copy()

    @property
    def pontos_de_vida(self):
        return self._pontos_de_vida
    @property
    def pontos_de_ataque(self):
        return self._pontos_de_ataque
    @property
    def quantidade_de_partes(self):
        return self._quantidade_de_partes
    @property
    def partes(self):
        return self._partes

    def ler_critico_da_parte(self, parte:str)->tuple[int]:
        '''
        Função que lê o ponto crítico da parte.
        '''
        # Achar a parte:
        for parte_ in self._partes:
            if parte_.ler_nome() == parte:
                return parte_.ler_ponto_critico()
    
    def ler_pontos_de_ataque(self) -> int:
        '''
        Função que lê os pontos de ataque de um monstro.
        '''
        return self._pontos_de_ataque

    def ler_partes(self) -> str:
        '''
        Função que lê as partes de um monstro.
        '''
        return self._partes

    def adicionar_parte(self, linha_de_texto:str)->None:
        '''
        Fução que recebe uma linha de texto e cria uma parte
        '''
        nome, fraquezas, dano_maximo, cx, cy = linha_de_texto.split(", ")

        parte = Parte(nome, fraquezas, int(dano_maximo), (int(cx), int(cy)))
        self._partes.append(parte)

    def receber_dano(self, parte:str, tipo_flecha:str, fx:int, fy:int) -> bool:
        '''
        Função que aplica o dano no monstro, de acordo com
        a parte acertada, o tipo de flecha e as coordenadas
        do acerto. Após isso, ela retorna se o monstro ainda
        está vivo.
        '''
        dano_recebido = self.calcular_dano(parte, tipo_flecha, (fx, fy))
        if self._pontos_de_vida - dano_recebido <= 0:
            self._pontos_de_vida = 0
            # Testar se o monstro ainda está vivo:
            return False
        else:
            self._pontos_de_vida = self._pontos_de_vida - dano_recebido
            return True

    
    def calcular_dano(self, parte_acertada:str, tipo_flecha:str, ponto_acertado:tuple[int]) -> int:
        '''
        Função que calcula o dano de determinada flechada de acordo com
        o tipo da flecha, a parte acertada e o ponto acertado.
        '''
        # localizar a parte acertada
        for parte in self._partes:
            if parte.ler_nome() == parte_acertada:
                return parte.calc_dano(tipo_flecha, ponto_acertado)
        
class Parte:
    def __init__(self, nome: str, fraquezas:str, dano_maximo:int, ponto_critico):
        self._nome = nome
        self._fraquezas = fraquezas
        self._dano_maximo = dano_maximo
        self._ponto_critico = ponto_critico
    @property
    def nome(self):
        return self._nome
    @property
    def fraquezas(self):
        return self._fraquezas
    @property
    def dano_maximo(self):
        return self._dano_maximo
    @property
    def ponto_critico(self):
        return self._ponto_critico
    
    def ler_ponto_critico(self) -> tuple[int]:
        '''
        Função que retorna o ponto critico da parte
        '''
        return self._ponto_critico

    def ler_nome(self) -> str:
        '''
        Função que lê o nome da parte.
        '''
        return self._nome

    def calc_dano(self, tipo_flecha:str, ponto_acertado:tuple[int]) -> int:
        '''
        Calcula o dano de uma flecha de acordo com seu tipo e com a parte acertada.
        '''
        #testar se se a flecha é da fraqueza
        if tipo_flecha == self._fraquezas or self._fraquezas == 'todas':
            d = abs(self._ponto_critico[0] - ponto_acertado[0]) + abs(self._ponto_critico[1] - ponto_acertado[1])
            dano_causado = self._dano_maximo - d
            if dano_causado < 0:
                return 0
            return dano_causado
        else:
            # Se a flecha não for do mesmo tipo que a fraqueza
            d = abs(self._ponto_critico[0] - ponto_acertado[0]) + abs(self._ponto_critico[1] - ponto_acertado[1])
            dano_causado = (self._dano_maximo - d)//2
            if dano_causado < 0:
                return 0
            return dano_causado


def main() -> None:
    vida = int(input())
    linha_flechas = input().split()
    flechas = {}
    num_flechas = 0
    for c in range(len(linha_flechas)//2):
        flechas[linha_flechas[2*c]] = int(linha_flechas[2*c+1])
        num_flechas += int(linha_flechas[2*c+1])
    flechas_restantes = num_flechas
    aloy = Aloy(vida, flechas)
    num_monstros_restantes = int(input())
    num_do_combate = 0
    while num_monstros_restantes != 0 and aloy.ler_vida() != 0 and flechas_restantes != 0:
        acertou_critico = False
        criticos_acertados:dict[int:dict[str:int]] = {}
        flechas_utilizadas = {}
        for flecha in flechas.keys():
            flechas_utilizadas[flecha] = 0
        aloy.curar()
        print(f'Combate {num_do_combate}, vida = {aloy.ler_vida()}')
        #resetar a vida
        flechas_restantes = num_flechas
        #adicionar os monstros
        monstros:list[Monstro] = []
        monstros_no_combate = int(input())
        for c in range (monstros_no_combate):
            vida, ataque, num_partes = list(map(int, input().split()))
            monstro = Monstro(vida, ataque, num_partes)
            for i in range(num_partes):
                monstro.adicionar_parte(input())
            monstros.append(monstro)
            criticos_acertados[monstros.index(monstro)] = {}
            for parte in monstro.ler_partes():
                criticos_acertados[monstros.index(monstro)][parte.ler_nome()] = 0

        todos_monstros = monstros.copy()
        #definir os alvos
        ha_monstros_a_derrotar = True
        while ha_monstros_a_derrotar and flechas_restantes > 0 and aloy.ler_vida() != 0:
            alvo, parte, tipo_flecha, fx, fy = input().split(sep=', ')
            flechas_restantes -= 1
            flechas_atiradas = num_flechas - flechas_restantes
            flechas_utilizadas[tipo_flecha] += 1
            monstro_vivo = todos_monstros[int(alvo)].receber_dano(parte, tipo_flecha, int(fx), int(fy))
            #testar se o ponto crítico foi acertado
            if (int(fx), int(fy)) == todos_monstros[int(alvo)].ler_critico_da_parte(parte):
                # Se o ponto critico tiver sido acertado
                criticos_acertados[int(alvo)][parte] += 1
                acertou_critico = True

            if not monstro_vivo:
                monstros.remove(todos_monstros[int(alvo)])
                monstro_vivo = True
                print(f'Máquina {alvo} derrotada')
            if monstros == []:
                ha_monstros_a_derrotar = False
            if flechas_atiradas % 3 == 0:
                #aloy receberá dano de todas as maquinas vivas
                for monstro in monstros:
                    dano_recebido = monstro.ler_pontos_de_ataque()
                    aloy.receber_dano(dano_recebido)

        num_monstros_restantes -= monstros_no_combate
        # mostrar vida após o combate
        print(f'Vida após o combate = {aloy.ler_vida()}')
        if aloy.ler_vida() != 0:
            # mostrar o numero de flechas utilizadas
            if flechas_restantes != 0:
                print('Flechas utilizadas:')
                for flecha, numero in flechas_utilizadas.items():
                    if numero > 0:
                        print(f'- {flecha}: {numero}/{aloy.ler_num_flecha(flecha)}')
                #mostrar os criticos acertados, por maquina
            if acertou_critico:
                print('Críticos acertados:')
                for n_monstro, dicionario_partes in criticos_acertados.items():
                    acertou_critico_maq = False
                    for n_vezes in dicionario_partes.values():
                        if n_vezes > 0: 
                            acertou_critico_maq = True
                            break
                    if acertou_critico_maq:
                        print(f'Máquina {n_monstro}:')
                        for parte, n_vezes in dicionario_partes.items():
                            if n_vezes > 0:
                                print(f'- {todos_monstros[n_monstro].ler_critico_da_parte(parte)}: {n_vezes}x')


        num_do_combate += 1

    if aloy.ler_vida() == 0:
        print('Aloy foi derrotada em combate e não retornará a tribo.')
    elif flechas_restantes == 0:
        print('Aloy ficou sem flechas e recomeçará sua missão mais preparada.')
    else:
        print('Aloy provou seu valor e voltou para sua tribo.')


main()